from bardapi import Bard
import os

from dotenv import load_dotenv
load_dotenv()

from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": 'eggeLzV7i_30102_2Uur1PXlMwBSlcTBNHs90FKGjJrtjFC7Kq7Eb0NxiRvL0E5cwRaeCg.',
    "__Secure-1PSIDTS": "sidts-CjEBPVxjSo70BUa0csTtja_MX1eRUJ_J3QnVojQ_ie9TyyH6VC8f3sQDicE_1DtNi1oCEAA",
  
}

bard = BardCookies(cookie_dict=cookie_dict)



def getResponse(prompt):

    response = bard.get_answer(prompt)

    return response['content']



