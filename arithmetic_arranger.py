def arithmetic_arranger(problems, *args):
  answ = False
  if args:
    answ = True
  if len(problems) > 5:
    return 'Error: Too many problems.'
  t, bot, top, l, total = '', [], [], [], []
  for i in problems:
    if '+' in i:
      t = '+'
    elif '-' in i:
      t = '-'
    else:
      return "Error: Operator must be '+' or '-'."
    if ((i.split(t)[0].strip()).isdigit() == False
        or (i.split(t)[1].strip()).isdigit() == False):
      return "Error: Numbers must only contain digits."
    if len((i.split(t)[0].strip())) > 4 or len((i.split(t)[1].strip())) > 4:
      return 'Error: Numbers cannot be more than four digits.'
    x = (max(len(i.split(t)[0].strip()), len(i.split(t)[1].strip())))
    top.append(f'{i.split(t)[0].strip(): >{x + 2}}')
    bot.append(f'{t: <2}{i.split(t)[1].strip(): >{x}}')
    t = ''
    for i in range(len(bot[-1])):
      t = t + '-'
    l.append(t)
    #answer
    if answ:
      tt = int((str(bot[-1])).replace(' ', ''))
      total.append(f'{int(str(top[-1]).strip()) + tt: >{len(l[-1])}}')

  top = '    '.join(top)
  bot = '    '.join(bot)
  l = '    '.join(l)
  total = '    '.join(total)

  if answ:
    print((f'{top}\n{bot}\n{l}\n{(total)}'))
    return (f'{top}\n{bot}\n{l}\n{(total)}')
  if not answ:
    return (f'{top}\n{bot}\n{l}')
