from selenium.webdriver import Firefox
import ipdb

def before_all(context):
    context.browser = Firefox()


def after_all(context):
    context.browser.quit()

def after_step(context, step):
    if step.status == 'failed':
        ipdb.sset_trace()
