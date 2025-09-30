from django.shortcuts import render

def kishore(request):
    power = 'I2R'
    if request.method == "POST":
        try:
            I = float(request.POST.get("intensity", 0))
            R = float(request.POST.get("resistance", 0))
            power = I**2 * R
            print("Current (I):", I)          # Debug print
            print("Resistance (R):", R)      # Debug print
            print("Calculated Power:", power) # Debug print
        except ValueError:
            power = "Invalid input"
            print("Error: Invalid input")     # Debug print
    return render(request, "math.html", {"power": power})

