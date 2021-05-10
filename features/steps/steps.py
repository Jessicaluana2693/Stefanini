from json import loads
from behave import given, when, then

@given('que eu esteja na página de cadastro')
def go_to_page(context):
    context.browser.get('http://prova.stefanini-jgr.com.br/teste/qa/')


@when('criar um usuário corretamente')
def create_user(context):
    texto_do_step = loads(context.text)

    context.browser.find_element_by_id('name').send_keys(texto_do_step['nome'])
    context.browser.find_element_by_id('email').send_keys(texto_do_step['email'])
    context.browser.find_element_by_id('password').send_keys(texto_do_step['senha'])
    context.browser.find_element_by_id('register').click()



@then(u'a {tabela} de usuários cadastrados deve ser exibida')
def check_user(context, tabela):
    assert 'João' in context.browser.find_element_by_id('tdUserName1').text
