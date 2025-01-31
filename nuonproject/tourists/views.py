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
import html
# import requests

from django.http import JsonResponse
import requests
import html

def get_pins(request):
    print('=============================-')
    print('API実行')
    tour_number = request.GET.get('tour_number', None) 
    print(f'取得した tour_number: {tour_number}')  # ログ出力で確認
    print("リクエストのクエリパラメータ:", request)  # デバッグ用

    # tour_number を取得
    if not tour_number:
        return JsonResponse({'error': 'tour_number is required'}, status=400)


    api_key = 'AIzaSyBZEV4yAriodr076SoPrK5LAoVkuOhRX78'
    geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    translate_url = 'https://translation.googleapis.com/language/translate/v2'

    # tour_number に紐づくピンのみ取得（修正）
    pins = Information_pin.objects.filter(tour_number=tour_number)

    data = []

    for pin in pins:
        print('========================================================================-')
        print('pin:', pin)

        # ジオコーディング
        geocode_params = {
            'address': pin.address,
            'key': api_key
        }
        geocode_response = requests.get(geocode_url, params=geocode_params)
        geocode_result = geocode_response.json()

        # レスポンスをログに記録
        print('Geocode API Response:', geocode_result)

        # ジオコーディング結果がOKか確認
        if geocode_result['status'] == 'OK' and 'geometry' in geocode_result['results'][0]:
            location = geocode_result['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
        else:
            latitude = None
            longitude = None

        # 翻訳処理
        translations = {}
        translations_explanation = {}

        for target_lang in ['en', 'zh', 'zh-TW', 'ko']:
            # 場所の翻訳
            translate_params = {
                'q': html.escape(pin.place),
                'source': 'ja',
                'target': target_lang,
                'key': api_key
            }
            translate_response = requests.get(translate_url, params=translate_params)
            translate_result = translate_response.json()
            print(f'Translation API Response for {target_lang}:', translate_result)  # 追加
            if 'data' in translate_result and 'translations' in translate_result['data']:
                translations[target_lang] = html.unescape(translate_result['data']['translations'][0].get('translatedText', ''))
            else:
                print(f'Translation failed for {target_lang}: {translate_result}')
                translations[target_lang] = ''

            # 説明の翻訳
            translate_params = {
                'q': html.escape(pin.explanation),
                'source': 'ja',
                'target': target_lang,
                'key': api_key
            }
            translate_response = requests.get(translate_url, params=translate_params)
            translate_result = translate_response.json()
            print(f'Translation API Response for {target_lang}:', translate_result)  # 追加
            if 'data' in translate_result and 'translations' in translate_result['data']:
                translations_explanation[target_lang] = html.unescape(translate_result['data']['translations'][0].get('translatedText', ''))
            else:
                print(f'Translation failed for {target_lang}: {translate_result}')
                translations_explanation[target_lang] = ''

        # 画像のURLを取得
        image_url = pin.image.url if pin.image else '/media/images/no_image.png'

        pin_data = {
            'information_pin_id': pin.information_pin_id,  # 案内ピン番号を追加
            'place_ja': pin.place,
            'place_en': translations['en'],
            'place_zh': translations['zh'],
            'place_zh-TW': translations['zh-TW'],
            'place_ko': translations['ko'],
            'explanation_ja': pin.explanation,
            'explanation_en': translations_explanation['en'],
            'explanation_zh': translations_explanation['zh'],
            'explanation_zh-TW': translations_explanation['zh-TW'],
            'explanation_ko': translations_explanation['ko'],
            'address_ja': pin.address,
            'latitude': latitude,
            'longitude': longitude,
            'image_url': image_url  # 画像URLを追加
        }

        print(pin_data)  # デバッグ用：APIレスポンスを確認
        data.append(pin_data)

    return JsonResponse(data, safe=False)
