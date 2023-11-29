from django.shortcuts import render
from .models import Laptop
from django.db.models import F, FloatField, ExpressionWrapper

# ... your other imports ...

def index(request):
    # Retrieve all laptops from the database
    laptops = Laptop.objects.all()

    # Prepare the context to pass to the template
    context = {
        "toplap": laptops,
    }

    # Render the index page with the laptop data
    return render(request, "index.html", context)

def tampil_laptop(request):
    # Call the SAW calculation function before displaying data to the user
    hitung_saw(request)

    # Retrieve laptop data after the SAW calculation
    laptops = Laptop.objects.all()

    # ... other view logic ...

    # Render the 'tampil_laptop' page with the updated laptop data
    return render(request, 'tampil_laptop.html', {'laptops': laptops})

def hitung_saw(request):
    # Retrieve all laptops from the database
    laptops = Laptop.objects.all()

    # Specify the ranges and values for each criterion
    rentang_ram = {'32 GB': 5, '16 GB': 4, '12 GB': 3, '8 GB': 2, '4 GB': 1}
    rentang_memori_internal = {'2 TB': 5, '1 TB': 4, '512 GB': 3, '256 GB': 2, '128 GB': 1}
    rentang_layar = {'17,3 inci': 5, '15,6 inci': 4, '14 inci': 3, '13,3 inci': 2, '13 inci': 1, '11,6 inci': 1}
    rentang_harga = {
        'Rp 27600000 - Rp 30000000': 1,
        'Rp 22200000 - Rp 27600000': 2,
        'Rp 16800000 - Rp 22200000': 3,
        'Rp 11400000 - Rp 16800000': 4,
        'Rp 6000000 - Rp 11400000': 5,
    }
    rentang_baterai = {
        '14000 mAh': 5,
        '12000 mAh': 4,
        '10000 mAh': 3,
        '9000 mAh': 2,
        '8000 mAh': 1,
        '7000 mAh': 1,
        '6000 mAh': 1,
    }

    # Specify the initial weights for each criterion
    bobot_ram = 0.2
    bobot_memori_internal = 0.2
    bobot_layar = 0.2
    bobot_harga = 0.2
    bobot_baterai = 0.2

    # Get input weights from the form (replace with actual form field names)
    input_bobot_ram = float(request.POST.get('bobot_ram', 1.0))
    input_bobot_memori_internal = float(request.POST.get('bobot_memori_internal', 1.0))
    input_bobot_layar = float(request.POST.get('bobot_layar', 1.0))
    input_bobot_baterai = float(request.POST.get('bobot_baterai', 1.0))
    input_bobot_harga = float(request.POST.get('bobot_harga', 1.0))

    # Determine the final weights for each criterion
    bobot_ramm = max(rentang_ram.values()) / input_bobot_ram
    bobot_memori_internall = max(rentang_memori_internal.values()) / input_bobot_memori_internal
    bobot_layarr = max(rentang_layar.values()) / input_bobot_layar
    bobot_hargaa = max(rentang_harga.values()) / input_bobot_harga
    bobot_bateraii = max(rentang_baterai.values()) / input_bobot_baterai
    
    print("Input Bobot RAM:", input_bobot_ram)
    print("Input Bobot Memori Internal:", input_bobot_memori_internal)
    print("Input Bobot Layar:", input_bobot_layar)
    print("Input Bobot Baterai:", input_bobot_baterai)
    print("Input Bobot Harga:", input_bobot_harga)

    print("Bobot Akhir RAM:", bobot_ramm)
    print("Bobot Akhir Memori Internal:", bobot_memori_internall)
    print("Bobot Akhir Layar:", bobot_layarr)
    print("Bobot Akhir Harga:", bobot_hargaa)
    print("Bobot Akhir Baterai:", bobot_bateraii)

    # Directly calculate SAW for each laptop using F expressions
    laptops.update(
        nilai_saw=F('ram') * (bobot_ramm * input_bobot_ram) +
                  F('memori_internal') * (bobot_memori_internall * input_bobot_memori_internal) +
                  F('layar') * (bobot_layarr * input_bobot_layar) + 
                  F('harga') * (bobot_hargaa * input_bobot_harga) +
                  F('baterai') * (bobot_bateraii * input_bobot_baterai)
    )
    
