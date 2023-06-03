import pandas as pd
current_df=pd.read_csv("./Star with gravity.csv")
current_df=current_df.drop('Unnamed: 0',1)
specialities=[]
for i in range(0,len(current_df)):
  sub_sp=[]
  try:
    if float(current_df['Distance'][i])<=100:
      sub_sp.append('Distance ')
  except:pass
  try:
    if float(current_df['Gravity'][i])>=150 and float(current_df['Gravity'][i])<=350:
      sub_sp.append('Gravity ')
  except:pass
  if len(sub_sp)==0:
    sub_sp.append('')
  specialities.append(sub_sp)
final_dict=[]
for i in range(0,len(current_df)):
  sub_fd={}
  sub_fd['Name']=current_df['Star Name'][i]
  sub_fd['Distance']=current_df['Distance'][i]
  sub_fd['Mass']=current_df['Mass'][i]
  sub_fd['Radius']=current_df['Radius'][i]
  sub_fd['Gravity']=current_df['Gravity'][i]
  sub_fd['Specialities']=specialities[i]
  final_dict.append(sub_fd)
print(final_dict)