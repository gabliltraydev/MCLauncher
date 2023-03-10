SET "DIR=%cd%"
SET "JAVA_HOME=C:\TropixeelLauncher\Minecraft1-18\runtime\java-runtime-beta\windows\java-runtime-beta"
SET "JAVA=%JAVA_HOME%\bin\javaw.exe"
SET MAX_MEM=2G
SET LIBRARIES=versions\1.18.2\natives
SET MAIN_CLASS=net.minecraft.client.main.Main
SET CLASSPATH=libraries\org\lwjgl\lwjgl-tinyfd\3.2.2\lwjgl-tinyfd-3.2.2.jar;libraries\com\mojang\patchy\2.2.10\patchy-2.2.10.jar;libraries\org\tlauncher\patchy\2.2.10\patchy-2.2.10.jar;libraries\com\mojang\text2speech\1.12.4\text2speech-1.12.4-natives-windows.jar;libraries\v1\objects\2e9a3e3107cca00d6bc9c97bf7d149cae163ef21\client.jar;libraries\com\google\guava\guava\31.0.1-jre\guava-31.0.1-jre.jar;libraries\net\java\dev\jna\jna\5.10.0\jna-5.10.0.jar;libraries\org\apache\logging\log4j\log4j-slf4j18-impl\2.17.0\log4j-slf4j18-impl-2.17.0.jar;libraries\org\lwjgl\lwjgl-glfw\3.2.2\lwjgl-glfw-3.2.2-natives-windows.jar;libraries\com\mojang\authlib\3.3.39\authlib-3.3.39.jar;libraries\com\mojang\blocklist\1.0.10\blocklist-1.0.10.jar;libraries\commons-logging\commons-logging\1.2\commons-logging-1.2.jar;libraries\it\unimi\dsi\fastutil\8.5.6\fastutil-8.5.6.jar;libraries\com\google\code\gson\gson\2.8.9\gson-2.8.9.jar;libraries\net\java\dev\jna\jna-platform\5.10.0\jna-platform-5.10.0.jar;libraries\org\lwjgl\lwjgl\3.2.2\lwjgl-3.2.2.jar;libraries\org\lwjgl\lwjgl-openal\3.2.2\lwjgl-openal-3.2.2-natives-windows.jar;libraries\org\lwjgl\lwjgl-tinyfd\3.2.2\lwjgl-tinyfd-3.2.2-natives-windows.jar;libraries\com\github\oshi\oshi-core\5.8.5\oshi-core-5.8.5.jar;libraries\com\google\guava\failureaccess\1.0.1\failureaccess-1.0.1.jar;libraries\net\sf\jopt-simple\jopt-simple\5.0.4\jopt-simple-5.0.4.jar;libraries\org\apache\logging\log4j\log4j-api\2.17.0\log4j-api-2.17.0.jar;libraries\org\lwjgl\lwjgl-openal\3.2.2\lwjgl-openal-3.2.2.jar;libraries\org\lwjgl\lwjgl-stb\3.2.2\lwjgl-stb-3.2.2-natives-windows.jar;libraries\org\slf4j\slf4j-api\1.8.0-beta4\slf4j-api-1.8.0-beta4.jar;libraries\org\tlauncher\authlib\3.3.392\authlib-3.3.392.jar;libraries\com\mojang\brigadier\1.0.18\brigadier-1.0.18.jar;libraries\commons-io\commons-io\2.11.0\commons-io-2.11.0.jar;libraries\com\mojang\datafixerupper\4.1.27\datafixerupper-4.1.27.jar;libraries\org\apache\httpcomponents\httpclient\4.5.13\httpclient-4.5.13.jar;libraries\com\ibm\icu\icu4j\70.1\icu4j-70.1.jar;libraries\com\mojang\javabridge\1.2.24\javabridge-1.2.24.jar;libraries\org\apache\logging\log4j\log4j-core\2.17.0\log4j-core-2.17.0.jar;libraries\com\mojang\logging\1.0.0\logging-1.0.0.jar;libraries\org\lwjgl\lwjgl-glfw\3.2.2\lwjgl-glfw-3.2.2.jar;libraries\io\netty\netty-all\4.1.68.Final\netty-all-4.1.68.Final.jar;libraries\com\mojang\text2speech\1.12.4\text2speech-1.12.4.jar;libraries\commons-codec\commons-codec\1.15\commons-codec-1.15.jar;libraries\org\apache\commons\commons-compress\1.21\commons-compress-1.21.jar;libraries\org\apache\commons\commons-lang3\3.12.0\commons-lang3-3.12.0.jar;libraries\org\apache\httpcomponents\httpcore\4.4.14\httpcore-4.4.14.jar;libraries\org\lwjgl\lwjgl\3.2.2\lwjgl-3.2.2-natives-windows.jar;libraries\org\lwjgl\lwjgl-jemalloc\3.2.2\lwjgl-jemalloc-3.2.2.jar;libraries\org\lwjgl\lwjgl-jemalloc\3.2.2\lwjgl-jemalloc-3.2.2-natives-windows.jar;libraries\org\lwjgl\lwjgl-opengl\3.2.2\lwjgl-opengl-3.2.2.jar;libraries\org\lwjgl\lwjgl-opengl\3.2.2\lwjgl-opengl-3.2.2-natives-windows.jar;libraries\org\lwjgl\lwjgl-stb\3.2.2\lwjgl-stb-3.2.2.jar
SET JAVA_OPTIONS=-Xmx%MAX_MEM% -XX:-UseAdaptiveSizePolicy -Xmn128M -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Djava.library.path=%LIBRARIES% -Dminecraft.launcher.brand=java-minecraft-launcher -Dminecraft.launcher.version=unknown -cp %CLASSPATH% %MAIN_CLASS%
setlocal enabledelayedexpansion

set /p NICK=<"C:\TropixeelLauncher\Minecraft1-18\nick.txt"
@echo !NICK! >"C:\TropixeelLauncher\Minecraft1-18\nick.txt"
set /p UUID=<"C:\TropixeelLauncher\Minecraft1-18\uuid.txt"
if "%UUID%"=="" (
  set "string=abcdef0123456789"
  set "uuid="
  for /L %%i in (1,1,32) do call :add
  @echo !uuid! >"C:\TropixeelLauncher\Minecraft1-18\uuid.txt"
  goto :continue

  :add
  set /a x=%random% %% 16 
  set uuid=%uuid%!string:~%x%,1!
  goto :eof
)
:continue

start "" /D "C:\TropixeelLauncher\Minecraft1-18" /I /HIGH "%JAVA%" %JAVA_OPTIONS% --version 1.18.2 --gameDir . --assetsDir assets --assetIndex 1.18 --accessToken 1337535510N --userType legacy --versionType release --uuid %uuid% --username %NICK% 