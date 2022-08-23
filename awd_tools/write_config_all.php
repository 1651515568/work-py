<?php
function write_file_php($file){
    $code = "<?php include('/home/team/workdir/monitor.php'); ?>\n";
    $code = $code.file_get_contents($file);
    file_put_contents($file,$code);
}
function getDir($path){
    $pass_array = array('/home/team/workdir/monitor.php','/home/team/workdir/write_config_all.php');
    if(!file_exists($path)){
        return [];
    }
    $handel = dir($path);
    $fileItem = [];
    if($handel){
        while(($file = $handel->read()) !== false){
            $newPath = $path . DIRECTORY_SEPARATOR . $file;
            $f = explode('.',$newPath);
            $f = end($f);
            if(is_dir($newPath) && $file != '.' && $file != '..'){
                getDir($newPath);
            }/**else if(is_file($newPath)) {
             //   echo $newPath.'<br>';
            }**/
            if($f == 'php'){
                if(in_array($newPath,$pass_array,TRUE)){
                    $status = 'pass';
                }else{
                    echo $newPath.'<br>';
                    write_file_php($newPath);
                }
            }
        }
    }
    $handel->close();
}
echo('开始写入配置...<br>');
$path = realpath('.');
getDir($path);
echo('配置写入完毕!<br>');