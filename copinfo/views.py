from django.http.response import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import exceptions
<<<<<<< HEAD
from .models import Cop,Data
=======
from .models import Cop
>>>>>>> af6a9cf2b0bf30d3186e3d7555bee2131c53e321
def info_view(request):
    if request.method=='GET':
        return render(request,'cop/info.html')
    elif request.method=='POST':
        copname=request.POST['copname']
        a=copname
        try:
            cop=Cop.objects.get(copname=copname)
<<<<<<< HEAD
            data=Data.objects.get(industry=cop.industry)
=======
>>>>>>> af6a9cf2b0bf30d3186e3d7555bee2131c53e321
        except Exception as e:
            print('not exist%s'%(e))
            return render(request,'cop/info.html',locals())

<<<<<<< HEAD
        if float(cop.solvency)>data.solvency:
            ana1="1.The EBITDA/interest expense ratio of the company is larger than the industry average, which means that the company's annual net operating income is sufficient to cover the annual interest expense and the company's short-term debt solvency is stronger than other companies in the same industry.  "
        if float(cop.solvency)<data.solvency:
            ana1="1.The EBITDA/interest expense ratio of the company is lower than the industry average, which means that the company's short-term debt solvency is weaker than other companies in the same industry, but the company's annual net operating income is still sufficient to cover the annual interest expense.  "
        if float(cop.profitmargin)>data.profitmargin:
            ana2="2.The company’s profit margin is higher than the industry average, indicating that the company’s profitability is strong and its competitiveness is higher than other companies in the same industry.  "
        if float(cop.profitmargin)<data.profitmargin:  
            ana2="2.The company's profit margin is lower than the industry average, indicating that the company's profitability is weak and its competitiveness is lower than other companies in the same industry.  "  
        if float(cop.incomegrowth)>data.incomegrowth:
            ana3="3.The company's operating income growth rate is higher than the industry average, which means that the company is expanding rapidly and has strong development potential.  "
        if float(cop.incomegrowth)<data.incomegrowth:
            ana3="3.The company’s operating income growth rate is lower than the industry average, which means that the company’s expansion rate is slow and it is in a mature or even declining development stage.  "
        if float(cop.profitgrowth)>data.profitgrowth:
            ana4="4.The company's profit growth rate is higher than the industry average. The company's growth momentum is strong and profitability is increasing.  "
        if float(cop.profitgrowth)<data.profitgrowth:
            ana4="4.The company's profit growth rate is lower than the industry average. The company's growth momentum is weaker than other companies in the industry and profitability is decreasing, which may affect the company's solvency in the future.  "
        if float(cop.cashdebt)>data.cashdebt:
            ana5="5.The company's money/interest-bearing liabilities ratio is higher than the industry average. The company's existing cash is sufficient to pay the company's interest-bearing liabilities, and the solvency is strongly guaranteed.  "
        if float(cop.cashdebt)<data.cashdebt:
            ana5="5.The company's money/interest-bearing liabilities ratio is lower than the industry average, but the company's existing cash is still sufficient to pay the company's interest-bearing liabilities, and the solvency is strongly guaranteed.  "
        if float(cop.cashflowdebt)>data.cashflowdebt:
            ana6="6.The company's operating cash flow/short-term debt ratio is higher than the industry average, which indicates that operating cash flow is sufficient.  "
        if float(cop.cashflowdebt)<data.cashflowdebt:
            ana6="6.The company's operating cash flow/short-term debt ratio is lower than the industry average, and the company's operating cash flow is not very sufficient.  "
        if float(cop.turnoverrate)>data.turnoverrate:
            ana7="7.The company's current asset turnover rate is higher than the industry average, showing that the company's operating capabilities are strong.  "
        if float(cop.turnoverrate)<data.turnoverrate:
            ana7="7.The company's current asset turnover rate is lower than the industry average, indicating that the company's operating capacity is weaker than other companies, which may be detrimental to debt repayment. If the company has a large amount of inventory, it may indicate that the company's products are not welcomed by the market and are difficult to sell.  "
        if float(cop.debtratio)>data.debtratio:
            ana8="8.The company’s debt-to-asset ratio is higher than the industry average, and the financial risk is relatively high. When there may be insufficient cash flow, the capital chain may break and the debt cannot be repaid in time, which may lead to corporate bankruptcy.  "
        if float(cop.debtratio)<data.debtratio:
            ana8="8.The company's asset-liability ratio is lower than the industry average, financial risks are relatively low, and the company's asset structure is healthy.  "


=======
        
>>>>>>> af6a9cf2b0bf30d3186e3d7555bee2131c53e321
        return render(request,'cop/info.html',locals())
        
        
        
