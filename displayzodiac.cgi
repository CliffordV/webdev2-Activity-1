#!C:/Users/VanderClifford/AppData/Local/Programs/Python/Python35-32/python.exe

import cgi
import cgitb
cgitb.enable()

print("Content-type: text/html \n")
print()

form = cgi.FieldStorage()
month = form.getvalue('month')
day = form.getvalue('day')	

print("""
	<!DOCTYPE html>
	<html>
		<head>
			<link rel="icon" type="image/png" href="zodiac-images.png">
			<title>Zodiac / Sign</title>
			<style>
				body {
					text-align: center;
					font-family: helvetica;
					background-image: url("background.png");
					background-size: 1366px 690px;
					background-repeat: no-repeat;
					position: fixed;
				    overflow-y: scroll;
				    width: 100%;
				}
				h2{
					font-family: 'Bangers', Georgia, Serif;
					font-size: 4em;
					color: rgba(255, 0, 0, 0.7);
				}
				h1{
					font-family: 'Bangers', Georgia, Serif;
					font-size: 4em;
					color: rgba(255, 0, 0, 0.7);
				img {
					width: 40%;
					height: 40%;
					margin: 0 0 0 15px;
				}
			</style>
		</head>

		<body>
		""")
	
if ((int(month)==12 and int(day) >= 22)or(int(month)==1 and int(day)<= 19)):
		print("<h2>Your Zodiac sign is </h2>")
		print("<h1>CAPRICORN</h1>")
		print("<br/><br/><br/><img src=\"capricorn.png\">")
		
elif ((int(month)==1 and int(day) >= 20)or(int(month)==2 and int(day)<= 17)):
		print("<h2>Your Zodiac sign is </h2>")
		print("<h1>AQUARIUS</h1>")
		print("<img src=\"aquarius.png\">")
		
elif ((int(month)==2 and int(day) >= 18)or(int(month)==3 and int(day)<= 19)):
		print("<h2>Your Zodiac sign is </h2>")
		print("<h1>PISCES</h1>")
		print("<img src=\"pisces.png\">")
		
elif ((int(month)==3 and int(day) >= 20)or(int(month)==4 and int(day)<= 19)):
		print("<h2>Your Zodiac sign is </h2>")
		print("<h1>ARIES</h1>")
		print("<img src=\"aries.png\">")
		
elif ((int(month)==4 and int(day) >= 20)or(int(month)==5 and int(day)<= 20)):
		print("<h2>Your Zodiac sign is </h2>")
		print("<h1>TAURUS</h1>")
		print("<img src=\"taurus.png\">")
		
elif ((int(month)==5 and int(day) >= 21)or(int(month)==6 and int(day)<= 20)):
		print("<h2>Your Zodiac sign is </h2>")
		print("<h1>GEMINI</h1>")
		print("<img src=\"gemini.png\">")
		
elif ((int(month)==6 and int(day) >= 21)or(int(month)==7 and int(day)<= 22)):
		print("<h2>Your Zodiac sign is </h2>")
		print("<h1>CANCER</h1>")
		print("<img src=\"cancer.png\">")
		
elif ((int(month)==7 and int(day) >= 23)or(int(month)==8 and int(day)<= 22)):
		print("<h2>Your Zodiac sign is </h2>")
		print("<h1>LEO</h1>")
		print("<img src=\"leo.png\">")
		
elif ((int(month)==8 and int(day) >= 23)or(int(month)==9 and int(day)<= 22)): 
		print("<h2>Your Zodiac sign is </h2>")
		print("<h1>VIRGO</h1>")
		print("<img src=\"virgo.png\">")
		
elif ((int(month)==9 and int(day) >= 23)or(int(month)==10 and int(day)<= 22)):
		print("<h2>Your Zodiac sign is </h2>")
		print("<h1>LIBRA</h1>")
		print("<img src=\"libra.png\">")
		
elif ((int(month)==10 and int(day) >= 23)or(int(month)==11 and int(day)<= 21)): 
		print("<h2>Your Zodiac sign is </h2>")
		print("<h1>SCORPIO</h1>")
		print("<img src=\"scorpio.png\">")
		
elif ((int(month)==11 and int(day) >= 22)or(int(month)==12 and int(day)<= 21)):
		print("<h2>Your Zodiac sign is </h2>")
		print("<h1>SAGITTARIUS</h1>")
		print("<img src=\"sagittarius.png\">")
		
print("<a href=\"enterBirthdate.html\"></a>")

print("""
		</body>
	</html>
	""")