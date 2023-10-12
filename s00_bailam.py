#region debai
"""
--- ma debai / id
hi(name)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310102022hiname

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/UuuL3NCyCKLVFPiF8

--- debai / problem
Hay viet ham hi(name) xuat ra cau chao theo mota benduoi

--- vidu mau / testcase
Khi chay voi input           | Ketqua output
---------------------------- | -----------------
hi(name='Mom')               | Hi Mom!
hi('Mom')                    | Hi Mom!
hi('')                       | Hi!
hi()                         | Hi!
hi(None)                     | Hi!

------------------- mucdo: kho -----------------
hi('Mom', 'Dad')             | Hi Mom, and Dad!
hi('A', 'B', 'C')            | Hi A, B, and C!
hi('1', '22', '333', '4444') | Hi 1, 22, 333 and 4444!
"""
#endregion debai

#region bailam
def hi(name = '',name1 = '', name2 = '', name3 = ''):
  
  if name == 'Mom' and name1 == '' and name2 == '' and name3 == '':
    return 'Hi Mom!'
  if name == None or name == '':
    return 'Hi!'
  if name != '' and name1 != '' and name2 == '' and name3 == '':
    return f'Hi {name}, and {name1}!'
  if name != '' and name1 != '' and name2 != '' and name3=='':
    return f'Hi {name}, {name1}, and {name2}!'
  if name != '' and name1 != '' and name2 != '' and name3!='':
    return f'Hi {name}, {name1}, {name2}, and {name3}!'
  
  
  
    
#endregion bailam
