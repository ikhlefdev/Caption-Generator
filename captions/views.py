from django.shortcuts import render

from captions.logic import generate_caption, generate_ai_caption

def home(request):
    generated_caption = None
    generated_ai_caption = None
    if request.method == 'POST':
        product = request.POST.get('product_name')
        platform = request.POST.get('platform')
        tone = request.POST.get('tone')
        feature = request.POST.get('feature')
        cta = request.POST.get('cta_type')



        # Generate caption based on the input values
        generated_caption = generate_caption(product, platform, tone, feature, cta)
        generated_ai_caption = generate_ai_caption(product, platform, tone, feature, cta)


    return render(request, 'captions/home.html', {'generated_caption': generated_caption, 'generated_ai_caption': generated_ai_caption})