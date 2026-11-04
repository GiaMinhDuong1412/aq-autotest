; Bộ cài AQ Auto Test (Inno Setup 6). GitHub Actions build: ISCC /DMyVer=<ver> /DSrcDir=<thư mục AQ-AutoTest đã giải nén> /DOutDir=<ra> app\aq-autotest.iss
; Cài cho người dùng hiện tại (không cần quyền admin) vào %LOCALAPPDATA%\Programs\AQ-AutoTest; dữ liệu du-lieu\ và rieng\ giữ lại khi cài đè / gỡ.
#ifndef MyVer
  #define MyVer "0.0.0"
#endif
#ifndef SrcDir
  #define SrcDir "..\build\AQ-AutoTest"
#endif
#ifndef OutDir
  #define OutDir "..\dist"
#endif

[Setup]
AppId={{5E0B7C1A-3D2F-4B8E-9A61-7C4D2E8F1A93}
AppName=AQ Auto Test
AppVersion={#MyVer}
AppVerName=AQ Auto Test {#MyVer}
AppPublisher=AQTech
DefaultDirName={localappdata}\Programs\AQ-AutoTest
DefaultGroupName=AQ Auto Test
DisableProgramGroupPage=yes
DisableWelcomePage=no
PrivilegesRequired=lowest
OutputDir={#OutDir}
OutputBaseFilename=AQ-AutoTest-Setup-{#MyVer}
SetupIconFile=aq-autotest.ico
UninstallDisplayIcon={app}\aq-autotest.ico
UninstallDisplayName=AQ Auto Test
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
CloseApplications=yes
RestartApplications=no

[Languages]
Name: "en"; MessagesFile: "compiler:Default.isl"

[Messages]
WelcomeLabel1=Cài đặt AQ Auto Test
WelcomeLabel2=Console kịch bản test Edusoft / Netweb của AQTech, chạy trên máy này (không cần cài Python hay Git).%n%nBản {#MyVer}. Sau khi cài, app tự cập nhật bằng nút phiên bản trên console.
FinishedHeadingLabel=Đã cài xong AQ Auto Test
FinishedLabel=Mở app bằng lối tắt "AQ Auto Test" trong Start Menu hoặc trên Desktop – console mở trong trình duyệt ở http://localhost:8788
ClickFinish=Bấm Finish để đóng.

[Tasks]
Name: "desktopicon"; Description: "Tạo lối tắt trên Desktop"; GroupDescription: "Lối tắt:"

[Files]
Source: "{#SrcDir}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "aq-autotest.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\AQ Auto Test"; Filename: "{app}\python\pythonw.exe"; Parameters: """{app}\launcher.py"""; WorkingDir: "{app}"; IconFilename: "{app}\aq-autotest.ico"; Comment: "Mở console AQ Auto Test"
Name: "{autodesktop}\AQ Auto Test"; Filename: "{app}\python\pythonw.exe"; Parameters: """{app}\launcher.py"""; WorkingDir: "{app}"; IconFilename: "{app}\aq-autotest.ico"; Comment: "Mở console AQ Auto Test"; Tasks: desktopicon

[Run]
Filename: "{app}\python\pythonw.exe"; Parameters: """{app}\launcher.py"""; WorkingDir: "{app}"; Description: "Mở AQ Auto Test"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}\phien-ban"
Type: filesandordirs; Name: "{app}\python"
Type: files; Name: "{app}\nhat-ky.txt"
