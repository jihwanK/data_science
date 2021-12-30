import modin.pandas as pd

filename = '/Users/ethan/Downloads/KMT2B_matrix.xlsx'
df = pd.read_excel(filename, dtype={'NGS_ID': 'int32', 'CpGisland': 'int32'})
print('read excel file')

col = list(df.columns)
col.remove('NGS_ID')
col.remove('CpGisland')

res_list = []

island_list = list(df['CpGisland'].drop_duplicates())
for idx, island in enumerate(island_list):
	for sample in col:
		sub_df = df[df['CpGisland'] == island][['NGS_ID', 'CpGisland', sample]]
		sub_df['sample'] = sample
		sub_df.columns = ['NGS_ID', 'CpGisland', 'Methylation_value' ,'Sample']
		res_list.append(sub_df)
	print(f'>>> {idx} {island} {(idx+1)/414*100}%')

res_df = pd.concat(res_list, ignore_index=True)
print('create dataframe done')

res_df.to_csv('result.tsv', sep='\t', index=False)
print('save it to tsv file')
