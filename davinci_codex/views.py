from django.shortcuts import render
import openai

def get_codex_result(prompt):
	openai.api_key = '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'

	response = openai.Completion.create(
	  engine="davinci-codex",
	  prompt=prompt,
	  temperature=0,
	  max_tokens=2048,
	  top_p=1,
	  frequency_penalty=0,
	  presence_penalty=0,
	  stop=["#"]
	)

	return response.choices[0].text


def home(request):
	if request.method == 'POST':
		if request.POST.get('prompt'):
			code = get_codex_result(request.POST.get('prompt'))
			#import pdb;pdb.set_trace()
		return render(request, 'data.html',context={
			"code": code, 'prompt': request.POST.get('prompt')
			})
	return render(request, 'home.html')

