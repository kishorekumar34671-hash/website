# Ex.07 Restaurant Website
# Date:03-10-2025
# AIM:
To develop a static Restaurant website to display the food items and services provided by them.

# DESIGN STEPS:
## Step 1:
Requirement collection.

## Step 2:
Creating the layout using HTML and CSS.

## Step 3:
Updating the sample content.

## Step 4:
Choose the appropriate style and color scheme.

## Step 5:
Validate the layout in various browsers.

## Step 6:
Validate the HTML code.

## Step 7:
Publish the website in the given URL.

# PROGRAM:

index.css
```
body {
    font-family: Arial, sans-serif;
    margin: 0;
    background-color: #fff7f5;
    color: #333;
}
header {
    background-color: #b33a3a; /* Primary color */
    color: white;
    padding: 20px;
    text-align: center;
}
nav {
    background-color: #333;
    text-align: center;
}
nav a {
    color: white;
    text-decoration: none;
    margin: 0 15px;
    padding: 8px;
    display: inline-block;
}
nav a:hover {
    background-color: #f2c57c; /* Accent color */
    color: #333;
}
section {
    padding: 40px;
    text-align: center;
}
h2 {
    color: #b33a3a;
    font-style:oblique;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}
.menu-grid, .team-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    max-width: 1000px;
    margin: 20px auto;
    text-align: center;
}
.card {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    font-style: italic;
    color:#b33a3a;
    text-shadow:#f2c57c;
}
.card img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 25px;
    align-items: center;
    border: #f2c57c;
    
}
footer {
    background-color:#333;
    color: white;
    
    text-align: center;
    padding: 15px;
}
contact-container {
            max-width: 800px;
            margin: 0 auto;
            text-align: left;
            padding: 20px;
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .contact-container h2 {
            text-align: center;
            color: #b33a3a;
        }
        .contact-container p {
            font-size: 18px;
            margin: 10px 0;
        }
        .contact-container b {
            color: #b33a3a;
        }

```

index.html
```
<!DOCTYPE html>
<html>
<head>
    <title>Buhari - Home</title>
    <link rel="stylesheet" href="index.css">
</head>
<body>
<header>
    <h1>Buhari Restaurant</h1>
</header>

<nav>
    <a href="index.html">Home</a>
    <a href="menu.html">Menu</a>
    <a href="admin.html">Administration</a>
    <a href="contact.html">Contact Us</a>
</nav>

<section>
    <img src="banner.jpg.png" alt="Restaurant Banner" style="width:80%; max-width:900px; border-radius:10px;">
    <h2>Welcome to Buhari</h2>
    <p>Authentic flavors, fresh ingredients, and a cozy dining experience.</p>
</section>

<footer>
    © Designed by Kishore Kumar B.
</footer>
</body>
</html>
```


menu.html
```

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>La Mesa - Menu</title>
    <link rel="stylesheet" href="index.css">
</head>
<body>
<header>
    <h1>Buhari Restaurant</h1>
</header>

<nav>
    <a href="index.html">Home</a>
    <a href="menu.html">Menu</a>
    <a href="admin.html">Administration</a>
    <a href="contact.html">Contact Us</a>
</nav>

<section>
    <h2>Our Menu</h2>
    <div class="menu-grid">
        <div class="card"><img src="food1.png.png"><p>Grilled Chicken - &#8377;420</p></div>
        <div class="card"><img src="food2.png.png"><p>Mushroom Pasta - ₹360</p></div>
        <div class="card"><img src="food3.png.png"><p>Paneer Tikka - ₹320</p></div>
        <div class="card"><img src="food4.png.png"><p>Margherita Pizza - ₹250</p></div>
        <div class="card"><img src="food5.png.png"><p>Veg Noodles - ₹200</p></div>
        <div class="card"><img src="food6.png.png"><p>Caesar Salad - ₹150</p></div>
        <div class="card"><img src="food7.png.png"><p>Chicken Curry - ₹320</p></div>
        <div class="card"><img src="food8.png.png"><p>Prawn Fry - ₹350</p></div>
        <div class="card"><img src="food9.png.png"><p>Pancakes - ₹160</p></div>
        <div class="card"><img src="food10.png.png"><p>Club Sandwich - ₹140</p></div>
        <div class="card"><img src="food11.png.png"><p>Fresh Juice - ₹100</p></div>
        <div class="card"><img src="food12.png.png"><p>Coffee - ₹80</p></div>
    </div>
</section>

<footer>
    © Designed by Kishore Kumar B.
</footer>
</body>
</html>
```

admin.html
```

<!DOCTYPE html>
<html>
<head>
    <title>Buhari - Administration</title>
    <link rel="stylesheet" href="index.css">
</head>
<body>
<header>
    <h1>Buhari Restaurant</h1>
</header>

<nav>
    <a href="index.html">Home</a>
    <a href="menu.html">Menu</a>
    <a href="admin.html">Administration</a>
    <a href="contact.html">Contact Us</a>
</nav>

<section>
    <h2>Meet Our Team</h2>
    <div class="team-grid">
        <div class="card"><img src="team1.jpg.png"><p>Person 1 - Head Chef</p></div>
        <div class="card"><img src="team2.jpg.png"><p>Person 2 - Manager</p></div>
        <div class="card"><img src="team3.jpg.png"><p>Person 3 - Sous Chef</p></div>
        <div class="card"><img src="team4.jpg.png"><p>Person 4 - HR Manager</p></div>
        <div class="card"><img src="team5.jpg.png"><p>Person 5 - Marketing Head</p></div>
        <div class="card"><img src="team6.jpg.png"><p>Person 6 - Floor Incharge</p></div>
    </div>
</section>

<footer>
    © Designed by Kishore Kumar B.
</footer>
</body>
</html>
```

contact.html
```

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Buhari - Contact Us</title>
    <link rel="stylesheet" href="index.css">
    
        
        
</head>
<body>

<header>
    <h1>Buhari Restaurant</h1>
</header>

<nav>
    <a href="index.html">Home</a>
    <a href="menu.html">Menu</a>
    <a href="admin.html">Administration</a>
    <a href="contact.html">Contact Us</a>
</nav>

<section>
    <div class="contact-container">
        <h2>Contact Us</h2>
        <p><b>Address:</b> No. 83, Anna Salai,Mount Road, Chennai,Tamil Nadu 600002</p>
        <p><b>Phone:</b> +91 98765 43210</p>
        <p><b>Email:</b> contact@lamesa.com</p>
        <p><b>Opening Hours:</b> Mon-Sun: 10:00 AM - 10:00 PM</p>
    </div>
</section>

<footer>
    © Designed by Kishore Kumar B.
</footer>

</body>
</html>
```



# OUTPUT:

![alt text](<Screenshot 2025-10-03 201748.png>)
![alt text](<Screenshot 2025-10-03 201831.png>)
![alt text](<Screenshot 2025-10-03 201847.png>)
![alt text](<Screenshot 2025-10-03 202054.png>)

# RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
