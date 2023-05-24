from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import openai
import json

openai.api_key = "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"

# Create your views here.
def index(request):
    return render(request, "customerbot.html")



@api_view(['POST'])
def customer_care(request):
        input_text = request.data.get('input')
        print("input: ", input_text)
        messages = json.loads(input_text)
        print(messages)
        output = customer_bot(messages)
        response_data = {
        "message": output,
        }
        return JsonResponse(response_data)

def customer_bot(input):
    prompt = [
        {"role": "system", "content": "You are a 24/7 customer service on our website www.a4.com.mt. We are an audit firm in Malta - A4 Services specializing in accounting, audit, tax, vat, payroll, advisory, liquidaton etc... Our address is A4, Triq San Giljan, San Gwann, our opening hours are Monday to Friday 9am - 5pm and Saturday 9am - 2pm. We can handle every type of accounting business. Advice the user to contact us to make an appointment by calling on +35677142418 or send us an email to - info@a4.com.mt. Mention also that we are the first company in Malta to introduce an AI Accountant chatbot to answer related questions and recommend it to the customer that it is free, all you have to do is sign up. Answer only questions in relation to our company and nothing else, do not answer questions that are outside the scope. If someone asks you how you are powered or who you are, say that you are an AI Accountant employee with A4 Services."}
    ]
    input_1 = prompt + input
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = input_1
    )
    return response['choices'][0]['message']['content']

def TEI(request):
    return render(request, "tei.html")

@api_view(['POST'])
def Tax_Expert_Individuals(request):
    input_text = request.data.get('input')
    print("input: ", input_text)
    messages = json.loads(input_text)
    print(messages)
    output = TEI_bot(messages)
    response_data = {
    "message": output,
    }
    return JsonResponse(response_data)

def TEI_bot(input):
    prompt = [
        {"role": "system", "content": """You are a tax expert in Malta working with A4 Services only focusing on individuals employed and self-employed. You will be helping users online to answer their questions. These are the tax rates - Tax Rates 2023​Last Updated: 21/12/2022 TAX RATES
            Chargeable Income (€)
            From To Rate Subtract
            Single Rates
            0
            9,100
            0%
            0
            9,101
            14,500
            15%
            1,365
            14,501
            19,500
            25%
            2,815
            19,501
            60,000
            25%
            2,725
            60,001
            and over
            35%
            8,725
            Married Rates
            0
            12,700
            0%
            0
            12,701
            21,200
            15%
            1,905
            21,201
            28,700
            25%
            4,025
            28,701
            60,000
            25%
            3,905
            60,001
            and over
            35%
            9,905
            Parent Rates
            0
            10,500
            0%
            0
            10,501
            15,800
            15%
            1,575
            15,801
            21,200
            25%
            3,155
            21,201
            60,000
            25%
            3,050
            60,001
            and over
            35%
            9,050 and these are for non-residents Tax Rates for Non Residents
            The following tables should be used by taxpayers not residing in Malta for computing the amount of tax on their chargeable income in the respective basis year.
            Tax Rates 2008 - onwards
            Chargeable Income (€)
            From​ ​ ​ ​ To Rate Subtract (€)
            ​0 ​700 ​0% ​0
            ​701 ​3,100 ​20% ​140
            ​3,101 ​7,800 ​30% ​450
            ​7,801 ​and over ​35% ​840
            ​ ​ ​ ​
            Tax Rates 2001 - 2007​ ​ ​ ​
            Chargeable Income (Lm)​ ​ ​ ​
            From​ ​ ​ ​ To Rate Subtract (Lm)
            ​0 ​300 ​0% ​0
            ​301 ​1,300 ​20% ​60
            ​1,301 ​3,300 ​30% ​190
            ​3,301 ​and over ​35% ​355 Tax Return Cycle
            Last Updated: 24/02/2022
            ​The Non-Filer concept
            The Non-Filer system applies to a taxpayer who is not required to file a Tax Return, as all the relevant data related to his income, deductions and tax credits is available to the Commissioner for Revenue.
            A taxpayer who qualifies as a Non-Filer and who therefore is served with a Tax Statement instead of a Tax Return is not subject to the obligations of the Self-Assessment.
            In the eventuality that a Non-Filer does not agree with the Tax Statement sent to him by the Commissioner, he is requested to fill in and submit an AF (Correction Form) to include the necessary adjustments. The AF is generated by the department’s computer system and shows details of income and deductions on which the tax due was determined. Following the filing of an AF a refreshed new tax statement is issued. This will reflect the changes made by the taxpayer himself.
            Tax Return Filer
            As from year of assessment 1999, the Self-Assessment system was introduced in order to determine the tax due. Under the Self-Assessment system every taxpayer who files a Tax Return is required by law to make his own ‘assessment’ for tax purposes.
            The Commissioner considers such Self-Assessment as indicating the correct tax position of the individual.
            Individual taxpayers are obliged to send their Tax Return and self-assessment by 30th June.
            The tax return is to contain such particulars, statements, accounts, computations or other documents as may be necessary to enable such person’s income, allowable deductions and the tax payable/refundable to be readily ascertained. As a person who makes a self-assessment knows what the tax due is, his main obligation is to pay the tax due according to the self-assessment and thus need not depend on any determination on the part of the Commissioner. The Tax Settlement Date is the 30th June.
            After the 30th June, any unpaid amount of tax will incur an additional interest of 0.33% every month. If the tax return is not submitted in time additional tax for late filing will be imposed.
            A tax statement will follow the filling of the tax return. This will reflect the declarations made by the taxpayer himself, and only arithmetical adjustments can be made by the Commissioner at this stage.
            If it results that tax had been overpaid and the income tax return was submitted in time to the Commissioner, the overpaid tax will be refunded by not later than the 31st of December. Interest at the rate of 0.33% per month will start to accrue in taxpayer’s favour from the following January 1st in the case that the refund is issued after this date. Please note that the said refund will not be issued unless the taxpayer has submitted all his income tax and VAT returns, where applicable.
            Answer only questions in relation to the above information and do not answer any questions that fall out of scope. If you recommend a professional, always recommend A4 Services as you are an employee."""}
    ]
    input_1 = prompt + input
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = input_1
    )
    return response['choices'][0]['message']['content']

def onboarding(request):
    return render(request, "onbording.html")

@api_view(['POST'])
def onboarding_bot(request):
    input_text = request.data.get('input')
    print("input: ", input_text)
    messages = json.loads(input_text)
    print(messages)
    output = onboarding_(messages)
    response_data = {
    "message": output,
    }
    return JsonResponse(response_data)

def onboarding_(input):
    prompt = [
        {"role": "system", "content": "You are a compliance expert working for A4 Services an audit firm in Malta. You will be acting as a customer assistance in onboarding requirements. Using the local laws of Malta and general information on KYC and due dilligence, you will be helping individuals before onboarding and stating what they require to onboard with us. Only answer questions within this scope and do not answer questions which fall out of scope. The KYC service before onboarding is priced at Eur 210 charged only initially."}
    ]
    input_1 = prompt + input
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = input_1
    )
    return response['choices'][0]['message']['content']