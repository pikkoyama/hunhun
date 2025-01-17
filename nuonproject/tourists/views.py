from django.http import JsonResponse
from django.views.generic import TemplateView
import requests  # requestsライブラリをインポート

class LanguageSelectView(TemplateView):
    template_name = 'LanguageSelect.html'

class TourmapView(TemplateView):
    template_name = 'Tourmap.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language'] = self.request.GET.get('language', 'ja')
        return context
    
# さくちゃん1/15
from django.http import JsonResponse
from guide.models import Information_pin  # guideアプリからインポート
# import requests

def get_pins(request):
    print('api実行')
    api_key = 'AIzaSyBZEV4yAriodr076SoPrK5LAoVkuOhRX78'
    geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    translate_url = 'https://translation.googleapis.com/language/translate/v2'
    pins = Information_pin.objects.all()
    data = []

    for pin in pins:
        print('========================================================================-')
        print('pin:',pin)
        # ジオコーディング
        geocode_params = {
            'address': pin.address,
            'key': api_key
        }
        geocode_response = requests.get(geocode_url, params=geocode_params)
        geocode_result = geocode_response.json()

        # レスポンスをログに記録
        print("Geocode API Response:", geocode_result)

        # ジオコーディング結果がOKか確認
        if geocode_result['status'] == 'OK' and 'geometry' in geocode_result['results'][0]:
            location = geocode_result['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
        else:
            # ジオコーディングに失敗した場合、nullのままとする
            latitude = None
            longitude = None

        # 翻訳処理
        translations = {}
        for target_lang in ['en', 'zh', 'zh-TW', 'ko']:
            translate_params = {
                'q': pin.explanation,
                'source': 'ja',
                'target': target_lang,
                'key': api_key
            }
            translate_response = requests.get(translate_url, params=translate_params)
            translate_result = translate_response.json()
            if 'data' in translate_result and 'translations' in translate_result['data']:
                translations[target_lang] = translate_result['data']['translations'][0].get('translatedText', '')
            else:
                print(f"Translation failed for {target_lang}: {translate_result}")
                translations[target_lang] = ''

        pin_data = {
            "explanation": pin.explanation,
            "explanation_en": translations['en'],
            "explanation_zh": translations['zh'],
            "explanation_zh_tw": translations['zh-TW'],
            "explanation_ko": translations['ko'],
            "address": pin.address,
            "place": pin.place,
            "latitude": latitude,
            "longitude": longitude,
        }

        print(pin_data)  # デバッグ用：APIレスポンスを確認
        data.append(pin_data)

    return JsonResponse(data, safe=False)