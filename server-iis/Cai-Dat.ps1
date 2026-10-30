# AQ Autotest Console - cài đặt trên IIS (chạy một lần qua CAI-DAT.cmd).
# Sau khi cài, IIS chạy aq-console-server.py; file này tự tải code mới nhất từ GitHub và tự cập nhật,
# không cần chạy lại gói cài khi có bản mới. Chạy lại CAI-DAT.cmd chỉ khi đổi cấu hình (đường dẫn, site, nhánh…).
param([switch]$Elevated)
$ErrorActionPreference = 'Stop'
$exitCode = 1
$transcript = $false

function Step($text) { Write-Host ''; Write-Host $text -ForegroundColor Cyan }

try {
    if (![Environment]::Is64BitProcess) { throw 'Hãy chạy CAI-DAT.cmd trên Windows 64-bit.' }
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    $admin = (New-Object Security.Principal.WindowsPrincipal($identity)).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    if (!$admin) {
        if ($Elevated) { throw 'Chưa được cấp quyền Administrator.' }
        Write-Host 'Windows sẽ hỏi quyền Administrator – chọn Yes.'
        $child = Start-Process -FilePath (Get-Process -Id $PID).Path -ArgumentList ('-NoProfile -ExecutionPolicy Bypass -File "' + $PSCommandPath + '" -Elevated') -Verb RunAs -Wait -PassThru
        exit $child.ExitCode
    }
    Start-Transcript -LiteralPath (Join-Path $PSScriptRoot 'cai-dat-log.txt') -Append | Out-Null
    $transcript = $true
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

    $s = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'CaiDat.settings.json') -Raw -Encoding UTF8 | ConvertFrom-Json
    $target = [IO.Path]::GetFullPath([string]$s.TargetPath)
    $pool = [string]$s.AppPool
    if ($s.Mode -notin @('app', 'site')) { throw 'Mode trong CaiDat.settings.json phải là "app" (thư mục con của site có sẵn) hoặc "site" (site riêng theo domain).' }
    if ($s.Mode -eq 'site' -and [string]::IsNullOrWhiteSpace($s.HostName)) { throw 'Mode "site" cần HostName (domain, vd autotest.aqtech.vn).' }

    Step '1/6 Kiểm tra IIS và AspNetCoreModuleV2...'
    Import-Module WebAdministration
    if (-not (Get-WebGlobalModule -Name 'AspNetCoreModuleV2' -ErrorAction SilentlyContinue)) {
        throw 'IIS chưa có AspNetCoreModuleV2. Cài ".NET Hosting Bundle" (máy đã chạy AQBuild thì đã có) rồi chạy lại.'
    }
    if ($s.Mode -eq 'app' -and -not (Test-Path ('IIS:\Sites\' + $s.SiteName))) { throw ('Không thấy site IIS "' + $s.SiteName + '".') }
    Write-Host ('Đích: ' + $target + '   Chế độ: ' + $s.Mode)

    Step '2/6 Chép aq-console-server.py...'
    New-Item -ItemType Directory -Force -Path $target | Out-Null
    $src = Join-Path $PSScriptRoot 'aq-console-server.py'
    if (!(Test-Path -LiteralPath $src)) { $src = Join-Path (Split-Path $PSScriptRoot -Parent) 'aq-console-server.py' }
    if (!(Test-Path -LiteralPath $src)) { throw 'Không thấy aq-console-server.py trong gói cài.' }
    $dst = Join-Path $target 'aq-console-server.py'
    if ([IO.Path]::GetFullPath($src) -ne [IO.Path]::GetFullPath($dst)) { Copy-Item -LiteralPath $src -Destination $dst -Force }

    Step '3/6 Python (bản nhúng, nằm gọn trong thư mục đích, không cài vào Windows)...'
    $py = Join-Path $target 'python\python.exe'
    if (!(Test-Path -LiteralPath $py)) {
        $zip = Join-Path $env:TEMP 'aq-python-embed.zip'
        Write-Host ('Tải ' + $s.PythonZip)
        Invoke-WebRequest -Uri $s.PythonZip -OutFile $zip -UseBasicParsing
        Expand-Archive -LiteralPath $zip -DestinationPath (Join-Path $target 'python') -Force
        Remove-Item -LiteralPath $zip -Force
    }
    $ver = & $py -c "import sys, ssl, http.server, zipfile; print(sys.version.split()[0])"
    if ($LASTEXITCODE -ne 0) { throw 'Python nhúng không chạy được.' }
    Write-Host ('Python ' + $ver)

    Step '4/6 Cấu hình (repo, nhánh, token GitHub)...'
    $conf = Join-Path $target 'aq-console-server.json'
    $c = [ordered]@{}
    if (Test-Path -LiteralPath $conf) {
        (Get-Content -LiteralPath $conf -Raw -Encoding UTF8 | ConvertFrom-Json).PSObject.Properties | ForEach-Object { $c[$_.Name] = $_.Value }
    }
    $c['repo'] = [string]$s.Repo
    $c['branch'] = [string]$s.Branch
    if ([string]::IsNullOrWhiteSpace([string]$c['token'])) {
        Write-Host 'Repo GitHub riêng tư cần token CHỈ-ĐỌC: github.com > Settings > Developer settings > Fine-grained tokens >'
        Write-Host 'Generate new token: Repository access = Only select repositories (chọn repo), Permissions > Contents = Read-only.'
        $c['token'] = (Read-Host 'Dán token (Enter để bỏ qua, điền sau vào aq-console-server.json)').Trim()
    }
    else { Write-Host 'Giữ token đã có.' }
    [IO.File]::WriteAllText($conf, ($c | ConvertTo-Json), (New-Object Text.UTF8Encoding($false)))

    $webConfig = @"
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <location path="." inheritInChildApplications="false">
    <system.webServer>
      <handlers>
        <remove name="WebDAV" />
        <remove name="aspNetCore" />
        <add name="aspNetCore" path="*" verb="*" modules="AspNetCoreModuleV2" resourceType="Unspecified" />
      </handlers>
      <modules>
        <remove name="WebDAVModule" />
      </modules>
      <aspNetCore processPath="$py" arguments="&quot;$dst&quot; --iis" hostingModel="outofprocess" startupTimeLimit="240" stdoutLogEnabled="false">
        <environmentVariables>
          <environmentVariable name="PYTHONUTF8" value="1" />
          <environmentVariable name="PYTHONUNBUFFERED" value="1" />
        </environmentVariables>
      </aspNetCore>
      <security>
        <requestFiltering>
          <requestLimits maxAllowedContentLength="52428800" />
        </requestFiltering>
      </security>
    </system.webServer>
  </location>
</configuration>
"@
    [IO.File]::WriteAllText((Join-Path $target 'web.config'), $webConfig, (New-Object Text.UTF8Encoding($false)))

    Step '5/6 IIS: App Pool, quyền thư mục, site/ứng dụng...'
    if (!(Test-Path ('IIS:\AppPools\' + $pool))) { New-WebAppPool -Name $pool | Out-Null; Write-Host ('Tạo App Pool ' + $pool) }
    $pp = 'IIS:\AppPools\' + $pool
    Set-ItemProperty $pp -Name managedRuntimeVersion -Value ''
    Set-ItemProperty $pp -Name startMode -Value 'AlwaysRunning'
    Set-ItemProperty $pp -Name processModel.idleTimeout -Value ([TimeSpan]::Zero)
    & icacls $target /grant ('IIS AppPool\' + $pool + ':(OI)(CI)M') /T /Q | Out-Null
    if ($LASTEXITCODE -ne 0) { throw 'Không cấp được quyền thư mục cho App Pool.' }

    $urls = @()
    if ($s.Mode -eq 'app') {
        $name = ([string]$s.AppPath).Trim('/')
        if (!$name) { throw 'AppPath không được để trống ở chế độ "app" (vd /aqautotest).' }
        if (Get-WebApplication -Site $s.SiteName -Name $name) {
            Set-ItemProperty ('IIS:\Sites\' + $s.SiteName + '\' + $name) -Name physicalPath -Value $target
            Set-ItemProperty ('IIS:\Sites\' + $s.SiteName + '\' + $name) -Name applicationPool -Value $pool
            Write-Host ('Cập nhật ứng dụng ' + $s.SiteName + '/' + $name)
        }
        else {
            New-WebApplication -Site $s.SiteName -Name $name -PhysicalPath $target -ApplicationPool $pool | Out-Null
            Write-Host ('Tạo ứng dụng ' + $s.SiteName + '/' + $name)
        }
        Set-ItemProperty ('IIS:\Sites\' + $s.SiteName + '\' + $name) -Name preloadEnabled -Value $true
        foreach ($b in (Get-WebBinding -Name $s.SiteName)) {
            $parts = $b.bindingInformation.Split(':')
            $h = if ($parts[2]) { $parts[2] } else { 'localhost' }
            $urls += ($b.protocol + '://' + $h + ':' + $parts[1] + '/' + $name + '/')
        }
    }
    else {
        $site = [string]$s.SiteName
        if (!(Test-Path ('IIS:\Sites\' + $site))) {
            New-Website -Name $site -PhysicalPath $target -ApplicationPool $pool -HostHeader $s.HostName -Port 80 | Out-Null
            Write-Host ('Tạo site ' + $site + ' (http://' + $s.HostName + ')')
        }
        else {
            Set-ItemProperty ('IIS:\Sites\' + $site) -Name physicalPath -Value $target
            Set-ItemProperty ('IIS:\Sites\' + $site) -Name applicationPool -Value $pool
            Write-Host ('Cập nhật site ' + $site)
        }
        Set-ItemProperty ('IIS:\Sites\' + $site) -Name applicationDefaults.preloadEnabled -Value $true
        if (-not (Get-WebBinding -Name $site -Protocol https -HostHeader $s.HostName)) {
            $hn = [string]$s.HostName
            $wild = '*.' + ($hn.Split('.', 2)[1])
            $cert = Get-ChildItem Cert:\LocalMachine\My | Where-Object { $_.NotAfter -gt (Get-Date) -and $_.HasPrivateKey -and ($_.DnsNameList.Unicode -contains $hn -or $_.DnsNameList.Unicode -contains $wild) } | Sort-Object NotAfter -Descending | Select-Object -First 1
            if ($cert) {
                New-WebBinding -Name $site -Protocol https -Port 443 -HostHeader $hn -SslFlags 1
                (Get-WebBinding -Name $site -Protocol https -HostHeader $hn).AddSslCertificate($cert.Thumbprint, 'My')
                Write-Host ('Gắn https bằng chứng chỉ ' + $cert.Subject + ' (hết hạn ' + $cert.NotAfter.ToString('dd/MM/yyyy') + ')')
            }
            else { Write-Host ('Chưa thấy chứng chỉ cho ' + $hn + ' trong máy – thêm binding https trong IIS Manager như các site khác.') -ForegroundColor Yellow }
        }
        $urls += ('http://' + $s.HostName + '/')
    }
    Restart-WebAppPool -Name $pool -ErrorAction SilentlyContinue
    if ((Get-WebAppPoolState -Name $pool).Value -ne 'Started') { Start-WebAppPool -Name $pool }

    Step '6/6 Khởi động và tải code lần đầu (tối đa 4 phút)...'
    foreach ($u in $urls) { try { Invoke-WebRequest -Uri $u -UseBasicParsing -TimeoutSec 20 | Out-Null } catch { } }
    $sha = Join-Path $target 'aq-console\app\.sha'
    $deadline = (Get-Date).AddMinutes(4)
    while (!(Test-Path -LiteralPath $sha) -and (Get-Date) -lt $deadline) {
        Start-Sleep -Seconds 5
        foreach ($u in $urls) { try { Invoke-WebRequest -Uri $u -UseBasicParsing -TimeoutSec 20 | Out-Null } catch { } }
    }
    $log = Join-Path $target 'aq-console\nhat-ky.txt'
    if (!(Test-Path -LiteralPath $sha)) {
        if (Test-Path -LiteralPath $log) { Get-Content -LiteralPath $log -Tail 8 -Encoding UTF8 }
        throw ('Console chưa tải được code (thường do thiếu token hoặc server không ra Internet). Sửa ' + $conf + ' rồi mở trang lại; nhật ký: ' + $log)
    }
    Write-Host ''
    Write-Host 'CAI DAT THANH CONG.' -ForegroundColor Green
    Write-Host ('Mở: ' + ($urls -join '  hoặc  '))
    $pw = Join-Path $target 'aq-console\rieng\mat-khau-admin-lan-dau.txt'
    if (Test-Path -LiteralPath $pw) { Write-Host ('Đăng nhập lần đầu: admin – mật khẩu trong ' + $pw + ' (đổi ở mục Hồ sơ rồi xoá file).') }
    Write-Host ('Từ giờ console tự cập nhật từ GitHub (nhánh ' + $s.Branch + ', 2 phút kiểm tra một lần). Nhật ký: ' + $log)
    $exitCode = 0
}
catch {
    Write-Host ('LỖI: ' + $_.Exception.Message) -ForegroundColor Red
}
finally {
    if ($transcript) { Stop-Transcript | Out-Null }
}
exit $exitCode
