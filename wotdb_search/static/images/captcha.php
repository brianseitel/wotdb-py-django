session_start(); //MUST START SESSION
header("Content-Type: image/png");
$string_length=5; //NUMBER OF CHARS TO DISPLAY
$rand_string='';
for($i=0;$i<$string_length;$i++)
{
  //PICK A RANDOM UPPERCASE LETTER USING ASCII CODE
  $rand_string.=chr(rand(65,90));
}//IMAGE VARIABLES
$width=100;
$height=36;
//INIT IMAGE
$img=imagecreatetruecolor($width, $height);
//ALLOCATE COLORS
$black=imagecolorallocate($img, 0, 0, 0);
$gray=imagecolorallocate($img, 200, 200, 200);
imagefilledrectangle($img, 0, 0, $width, $height, $gray);
//REPLACE THIS WITH THE FONT YOU UPLOAD
$font='Justus-Roman.ttf';
$font_size=16;
//CALC APPROX LOCATION FOR TEXT
$y_value=($height/2)+($font_size/2);
$x_value=($width-($string_length*$font_size))/2;
//DRAW STRING USING TRUE TYPE FUNCTION
imagettftext($img, $font_size, 0, $x_value,
    $y_value, $black, $font, $rand_string);
$_SESSION['encoded_captcha']=md5($rand_string);
//OUTPUT IMAGE HEADER AND SEND TO BROWSER

imagepng($img);

?>