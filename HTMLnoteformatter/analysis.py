import glob
import json

 
text1 = '''
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="x-apple-disable-message-reformatting">
  <title></title>
  <!--[if mso]>
  <noscript>
    <xml>
      <o:OfficeDocumentSettings>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
  </noscript>
  <![endif]-->
  <style>
    table, td, div, h1, p {font-family: Arial, sans-serif;}
  </style>
</head>
<body style="margin:0;padding:0;">
  <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
    <tr>
      <td align="center" style="padding:0;">
        <table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
          <tr>
            <td align="center" style="padding:10px 0 30px 0;background:#47a2a4;">
            <img src= "../logo/test.png" alt="" width="200"  style="height:auto;display:block;" />
              
            </td> 
          </tr>
          <tr>
            <td style="padding:36px 30px 42px 30px;">
              <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                <tr>
                  <td style="padding:0 0 36px 0;color:#153643;">
                    <h1 style="font-size:24px;margin:0 0 20px 0;font-family:Arial,sans-serif;text-align: center"font-weight: bold>Lecture Notes</h1>
                    <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">Notes created from Physics Lectures using key words and created Wikipedia links from key words</p>
                    <p style="margin:0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;"><a href="https://github.com/mingyeeee/Stormhacks2022" style="color:#ee4c50;text-decoration:underline;">Notes Generated using NoteAI</a></p>
                  </td>
                </tr>


                <tr>
                  <td style="padding:0;">
                    <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
                      
            

                    
'''                        

end = '''
</table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td style="padding:30px;background:#47a2a4;">
              <table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;font-size:9px;font-family:Arial,sans-serif;">
                <tr>
                  <td style="padding:0;width:50%;" align="left">
                    <p style="margin:0;font-size:14px;line-height:16px;font-family:Arial,sans-serif;color:#ffffff;">
                      &reg; Ottawa, Canada 2021<br/><a href="https://github.com/mingyeeee/Stormhacks2022" style="color:#ffffff;text-decoration:underline;">StormHacks2022</a>
                    </p>
                  </td>

                    <td style="padding:0;width:50%;" align="left">
                    <p style="margin:0;font-size:14px;line-height:16px;font-family:Arial,sans-serif;color:#ffffff;">
                      &reg; Ottawa, Canada 2021<br/>Improving lecture engagement by assisting notetaking using speech to audio, machine learning and wikipedia.</a>
                    </p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>

'''
def listmaker(txt):
  d = open(txt)
  read_file = d.read().split()
  return read_file

def list_to_string(lst):
  out = ""
  for i in lst:
    out += i + "\n" 
  return out

for file in glob.glob('/Users/brevinbaskaran/Stormhacks2022/HTMLnoteformatter/*.png'):
  if file == "/Users/brevinbaskaran/Stormhacks2022/HTMLnoteformatter/acceleration.png":
    links = listmaker("/Users/brevinbaskaran/Stormhacks2022/HTMLnoteformatter/acceleration_links.txt")
    text1 = text1 + '''<tr>
                        <td style="width:260px;padding:0;vertical-align:top;color:#153643;">
                        <p style="margin:0 0 25px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;font-weight: bold">Acceleration</p>
                          <p style="margin:0 0 25px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;"><img src="''' + file +'''" alt="" width="400" style="height:auto;display:block;" /></p>
                          <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">'''+ list_to_string(links) +'''</p>
                          
                        </td>
                       
                      </tr>'''
  elif file == "/Users/brevinbaskaran/Stormhacks2022/HTMLnoteformatter/displacement.png":
    links = listmaker("/Users/brevinbaskaran/Stormhacks2022/HTMLnoteformatter/displacement_links.txt")
    text1 = text1 + '''<tr>
                        <td style="width:260px;padding:0;vertical-align:top;color:#153643;">
                          <p style="margin:0 0 25px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;font-weight: bold">Displacement</p>
                          <p style="margin:0 0 25px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;"><img src="''' + file +'''" alt="" width="400" style="height:auto;display:block;" /></p>
                          <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">'''+ list_to_string(links) +'''</p>
                          
                        </td>
                       
                      </tr>'''
  elif file == "/Users/brevinbaskaran/Stormhacks2022/HTMLnoteformatter/kinematics.png":
    links = listmaker("/Users/brevinbaskaran/Stormhacks2022/HTMLnoteformatter/kinematics_links.txt")
    text1 = text1 + '''<tr>
                        <td style="width:260px;padding:0;vertical-align:top;color:#153643;">
                        <p style="margin:0 0 25px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;font-weight: bold">Kinematics</p>
                          <p style="margin:0 0 25px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;"><img src="''' + file +'''" alt="" width="400" style="height:auto;display:block;" /></p>
                          <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">'''+ list_to_string(links) +'''</p>
                          
                        </td>
                       
                      </tr>'''
  else:
    text1 = text1 + '''<tr>
                        <td style="width:260px;padding:0;vertical-align:top;color:#153643;">
                        <p style="margin:0 0 25px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;font-weight: bold">Equation</p>
                          <p style="margin:0 0 25px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;"><img src="''' + file +'''" alt="" width="400" style="height:auto;display:block;" /></p>
                          <p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;"></p>
                          
                        </td>
                       
                      </tr>'''
   
text1 = text1 + end



with open("index.html", "w") as outputfile:
	outputfile.write(text1)
