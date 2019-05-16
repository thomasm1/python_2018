<?php
$error = ""; 
$successMessage = "";
$projectNumber = "project Mars reader 1096-1";
$date = 3;
$nth = "nth";
$user = "user";
$tmmNumber = "5055087707";
$guestNumbers= array(5055087707, 5054637256, 5051234567);
$tmmName = "Thomas M. Maestas";
$louisName = "Louis P.";
$tmmEmail = "thomas.maestas@hotmail.com";
$tmmURL = "http://www.thomasmaestas.net";
$tmmCalculation = $tmmNumber * 31 /97 + 4;
$myArray = array("Hello", "My name is $tmmName.");

echo "
<!DOCTYPE html><html><head> 
 <meta charset=\"utf-8\">

 <style type=\"text/css\">

 body{

opacity:.85;

background-image:url(\"bluechipTile.jpg\");



 };

 h2,h3{

     text-align:center;

 };

 #container{

    margin-left:auto;

    width:80%;

    padding:20px;

    margin-right:auto;

    border:1px, solid, blue ;

    opacity:.9;

     background:steelblue;

 };

 </style>

 <meta charset=\"utf-8\">

 <script src=\"marsreader.js\"></script>

 <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js\"></script>

 <title>Mars Reader APOD call</title>

 </head>  <body style=\"color:white;background:darkgray;\" >

 <div id =\"container\">

 ";

  

if ($user == "user") {

    echo "<hr><br /><h3>Welcome Guest.</h3>";

 } else {

        echo "<hr><br /><h3>Welcome New Guest</h3>";

    };



echo " <br /><br /><br />";



if ($date <= 3 || $user == "user") {

    echo "  <h3>Welcome, Mars Report $projectNumber has not today updated with Mars report</h3>";

} else {

    echo " <h3>Welcome, Mars Report $projectNumber has today updated with Mars report</h3>";

};



echo "<hr><br /><br /><br />";



echo "<h2>Mars Reader</h2><h4>Greetings!</h4>

<h5>Today's NASA Report. This Twython Mars Weather Broadcast brought to you by

 $tmmName.<br /> This project $projectNumber is the $nth broadcast.</h5><br />";



 echo " <script type=\"text/javascript\"> var url = \"https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo\";

  $.ajax({

   url: url,

   success: function(result){

   if(\"copyright\" in result) {

     $(\"#copyright\").text(\"Image Credits: \" + result.copyright);

   }

   else {

     $(\"#copyright\").text(\"Image Credits: \" + \"Public Domain\");

   }

   

   if(result.media_type == \"video\") {

     $(\"#apod_img_id\").css(\"display\", \"none\"); 

     $(\"#apod_vid_id\").attr(\"src\", result.url);

   }

   else {

     $(\"#apod_vid_id\").css(\"display\", \"none\"); 

     $(\"#apod_img_id\").attr(\"src\", result.url);

   }

   $(\"#reqObject\").text(url);

   $(\"#returnObject\").text(JSON.stringify(result, null, 4));  

   $(\"#apod_explaination\").text(result.explanation);

   $(\"#apod_title\").text(result.title);

 }

 });

 </script>

 ";

 

 echo "<hr><b>API URL:    POST /api.example.com/foo?callbackURL=http://my.server.com/bar</b>

 <pre id=\"reqObject\"></pre> 

 <img id=\"apod_img_id\" width=\"250px\"/> 

 <iframe id=\"apod_vid_id\" type=\"text/html\" width=\"640\" height=\"385\" frameborder=\"0\"></iframe>

 <p id=\"copyright\"></p> 

 <h3 id=\"apod_title\"></h3>

 <p id=\"apod_explaination\"></p>

 <br/>

 <b>Return Object:</b>

 <pre id=\"returnObject\"></pre>";





 

echo "</p><br />Thank you for visiting the NASA-updated Mars Weather Reader Site. <br />Brought to you by 

Louis P. and Thomas Maestas.</p><br /></div></body>  </html>";  

?>
