from django.shortcuts import render
# Create your views here.
def home(request):
    return render (request, 'home.html')
def tracker(request):
    result = None
    if request.method == 'POST':
        try:
            allowance = float(request.POST.get('allowance', 0))
            food = float(request.POST.get('food', 0))
            transport = float(request.POST.get('transport', 0))
            airtime = float(request.POST.get('airtime', 0))
            entertainment = float(request.POST.get('entertainment', 0))
            other = float(request.POST.get('other', 0))

            total_spent = food + transport + airtime + entertainment + other
            remaining = allowance - total_spent
            percent_spent = round((total_spent / allowance) * 100, 1) if allowance > 0 else 0

            if remaining < 0:
                status = 'danger'
                message = f"You're R{abs(remaining):.2f} over budget! Time to cut back."
            elif percent_spent > 75:
                status = 'warning'
                message = f"You've spent {percent_spent}% of your allowance. Be careful!"
            else:
                status = 'good'
                message = f"Great job! You still have R{remaining:.2f} left. Keep it up!"

            result ={
                'allowance': allowance,
                'food': food,
                'transport': transport,
                'airtime': airtime,
                'entertainment': entertainment,
                'other': other,
                'total_spent': total_spent,
                'remaining': remaining,
                'percent_spent': percent_spent,
                'status': status,
                'message': message,
            }
        except ValueError:
            result = None
    return render(request, 'tracker.html', {'result': result})
def tips(request):
    tips_data = {
        'transport': [
            "Use a monthly taxi or bus pass if available - it is cheaper than paying daily.",
            "Walk short distances when it is safe. It saves money and keeps you fit.",
            "Share rides with classmates to split costs.",
            "Plan your trips - avoid unnecessary back nd forth travel.",
        ],
        'food': [
            "Cook at home instead of buying takeaways every day.",
            "Buy in bulk with friends - split a big pack of rice or pasta.",
            "Eat before you go out so you are not tempted to buy expensive food.",
            "Look for student meal deals near campus-many places offer discounts.",
        ],
        'airtime': [
            "Use WhatsApp on Wi-Fi instead of spending airtime on calls.",
            "Buy data bundles - they are cheaper than pay-as-you-go data.",
            "Connect to campus or library Wi-Fi for heavy browsing.",
            "Turn off background app refresh to save your data bundle.",
        ],
        'saving': [
            "Save at least 10% of your allowance every month, no matter what.",
            "Open a free student bank account with no monthly fees.",
            "Set a savings goal-even R50 per month adds up to R600 a year.",
            "Avoid lending money you cannot afford to lose.",
        ],
    }
    return render(request, 'tips.html', {'tips_data': tips_data})
def about(request):
    return render(request, 'about.html')
                