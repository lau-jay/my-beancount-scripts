import re

import dateparser


def get_eating_account(from_user, description, time=None):
    if time == None or not hasattr(time, 'hour'):
        return 'Expenses:Food:Others'
    elif time.hour <= 3 or time.hour >= 21:
        return 'Expenses:Food:Others'
    elif time.hour <= 10:
        return 'Expenses:Food:Breakfast'
    elif time.hour <= 16:
        return 'Expenses:Food:Lunch'
    else:
        return 'Expenses:Food:Supper'


def get_apple_account(from_user, description, time=None):
    if "苹果电子" in description or "苹果在线商店" in from_user:
        return "Expenses:Apple:Device"
    return "Expenses:Apple:Server"



def get_credit_return(from_user, description, time=None):
    return "Assets:Bank:CMB:Card4738:ZZY"


public_accounts = [
    'Assets:Company:Alipay:StupidAlipay'
]

credit_cards = {
    '招商银行': 'Liabilities:CreditCards:CMB',
}

accounts = {
    "余额宝": 'Assets:Company:Alipay:MonetaryFund',
    '余利宝': 'Assets:Bank:MyBank',
    '花呗': 'Liabilities:Company:Huabei',
    '建设银行': 'Liabilities:CreditCard:CCB',
    '零钱': 'Assets:Balances:WeChat',
}

descriptions = {
    #'滴滴打车|滴滴快车': get_didi,
    '信用卡自动还款|信用卡还款|手机银行还款': get_credit_return,
    '外卖订单': get_eating_account,
    '美团订单': get_eating_account,
    '上海交通卡发行及充值': 'Expenses:Transport:Card',
    '地铁出行': 'Expenses:Traffic:Subway',
    '高德打车': 'Expenses:Traffic:Taxi',
    '火车票': 'Expenses:Travel:Transport',
    '铁路网络': 'Expenses:Travel:Transport',
    'App Store|云上艾珀': 'Expenses:Apple:Server',
    '苹果电子产品': "Expenses:Apple:Device",
    '上海拉扎斯': get_eating_account,
    '医院': "Expenses:Health:Hospital",
    '上海朔羡网络': "Expenses:EasyHouse305:Rent",
    '上海梯辟': "Expenses:EasyHouse305:Utility",
    '上海玄霆娱乐': "Expenses:Play:Reading",
    '美宜': "Expenses:Food:Drink",
    '友琪': "Expenses:Food:Drink",
    '宠物': "Expenses:DogYogurt:Others",
    '金百味': "Expenses:Food:Dinner"
}

anothers = {
    '苹果在线商店': get_apple_account,
}

incomes = {
    '余额宝.*收益发放': 'Income:Trade:PnL',
}

description_res = dict([(key, re.compile(key)) for key in descriptions])
another_res = dict([(key, re.compile(key)) for key in anothers])
income_res = dict([(key, re.compile(key)) for key in incomes])
