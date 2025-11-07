<?php
# Mansooj Loader — internal

function _detect_lib(): string {
    $sysname = strtolower(PHP_OS_FAMILY);
    $base = __DIR__ . "/../lib";

    if (strpos($sysname, 'darwin') !== false || $sysname === 'darwin' || $sysname === 'macos') {
        $path = "$base/macos/mansoojlib.dylib";
    } elseif ($sysname === 'linux') {
        $path = "$base/linux/mansoojlib.so";
    } elseif ($sysname === 'windows') {
        $path = "$base/windows/mansoojlib.dll";
    } else {
        throw new Exception("Unsupported platform: $sysname");
    }

    if (!file_exists($path)) {
        throw new Exception("Mansooj library not found at: $path");
    }

    return realpath($path);
}

$LIB_PATH = _detect_lib();
$core = $LIB_PATH;  # placeholder handle, loaded in actual binding

return [
    "core" => $core,
    "LIB_PATH" => $LIB_PATH
];
?>
