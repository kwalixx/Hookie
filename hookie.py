from requests import post

class Hookie:
  def __init__(self):
    self.hook_url = ''
    
  def spam(self, nb_req):
    """spam 
    :param nb_req: The number of request to send
    """
    for i in range(nb_req):
      r = post(self.hook_url, params={content: "@everyone"})
    
