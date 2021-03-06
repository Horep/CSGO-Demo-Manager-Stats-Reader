import pandas as pd
import re
df = pd.read_excel(r'export-21-05-29-10-50-09.xlsx', sheet_name="Players")
my_name = r"defuzr"
sub_df = df[df['Name'].str.match(my_name, flags=re.I)]
longthing = "-"*60

output = []
output.append(f"Name: {sub_df.iloc[0]['Name']}")
output.append(longthing)
output.append(f"K/A/D: {sub_df.iloc[0]['Kills']} / {sub_df.iloc[0]['Assists']} / {sub_df.iloc[0]['Deaths']}")
output.append(f"KD Ratio: {sub_df.iloc[0]['K/D']} ({round(df['K/D'].mean(),2)})")
output.append(f"Rating: {sub_df.iloc[0]['Rating']} ({round(df['Rating'].mean(),2)})")
output.append(f"Headshot %: {sub_df.iloc[0]['HS%']}% ({round(df['HS%'].mean(),2)})")
output.append(f"Number of MVPs: {sub_df.iloc[0]['MVP']}")
output.append(f"Kills per round: {sub_df.iloc[0]['KPR']} ({round(df['KPR'].mean(),2)})")
output.append(f"Assists per round: {sub_df.iloc[0]['APR']} ({round(df['APR'].mean(),2)})")
output.append(f"Deaths per round: {sub_df.iloc[0]['DPR']} ({round(df['DPR'].mean(),2)})")
output.append(f"Average Damage per round: {sub_df.iloc[0]['ADR']} ({round(df['ADR'].mean(),2)})")
output.append(longthing)
output.append(f"K/A/D avg.: {round(sub_df.iloc[0]['Kills']/sub_df.iloc[0]['Match'],2)} / {round(sub_df.iloc[0]['Assists']/sub_df.iloc[0]['Match'], 2)} / {round(sub_df.iloc[0]['Deaths']/sub_df.iloc[0]['Match'], 2)}")
output.append(f"Average No. MVPs: {round(sub_df.iloc[0]['MVP']/sub_df.iloc[0]['Match'],2)}")
output.append(f"Average Score: {round(sub_df.iloc[0]['Score']/sub_df.iloc[0]['Match'],2)}")
output.append(f"Average Headshots: {round(sub_df.iloc[0]['HS']/sub_df.iloc[0]['Match'],2)}")
output.append(f"Average Entry kill win: {round(sub_df.iloc[0]['Entry kill win']/sub_df.iloc[0]['Match'],2)}")
output.append(f"Average Entry kill loss: {round(sub_df.iloc[0]['Entry kill lost']/sub_df.iloc[0]['Match'],2)}")
output.append(f"Average No. Flashbangs thrown: {round(sub_df.iloc[0]['Flashbang thrown']/sub_df.iloc[0]['Match'],2)}")
output.append(f"Average No. Smokes thrown: {round(sub_df.iloc[0]['Smoke thrown']/sub_df.iloc[0]['Match'],2)}")
output.append(f"Average No. HE's thrown: {round(sub_df.iloc[0]['HE thrown']/sub_df.iloc[0]['Match'],2)}")
output.append(f"Average No. Molly/Incen thrown: {round((sub_df.iloc[0]['Molotov thrown'] + sub_df.iloc[0]['Incendiary thrown'])/sub_df.iloc[0]['Match'],2)}")
output.append(f"Average No. Decoy's thrown: {round(sub_df.iloc[0]['Decoy thrown']/sub_df.iloc[0]['Match'],2)}")
output.append(longthing)
output.append(f"5K: {sub_df.iloc[0]['5K']}")
output.append(f"4K: {sub_df.iloc[0]['4K']}")
output.append(f"3K: {sub_df.iloc[0]['3K']}")
output.append(f"2K: {sub_df.iloc[0]['2K']}")
output.append(f"1K: {sub_df.iloc[0]['1K']}")
output.append(longthing)
output.append(f"Matches played: {sub_df.iloc[0]['Match']} ({round(df['Match'].mean(),2)})")
output.append(f"Rounds Played: {sub_df.iloc[0]['Rounds']} ({round(df['Rounds'].mean(),2)})")
output.append(f"Avg. Rounds Played: {round(sub_df.iloc[0]['Rounds'] / sub_df.iloc[0]['Match'],2)}")
output.append(f"Average Time to Death: {sub_df.iloc[0]['ATD (s)']} seconds ({round(df['ATD (s)'].mean(),2)})")
output.append(longthing)
output.append(f"Trade Kills: {sub_df.iloc[0]['Trade Kill']}")
output.append(f"% of Kills that are trades: {100*sub_df.iloc[0]['Trade Kill']/sub_df.iloc[0]['Kills']:.2f}%")
output.append(f"Traded Deaths: {sub_df.iloc[0]['Trade Death']}")
output.append(f"% of deaths traded: {100*sub_df.iloc[0]['Trade Death']/sub_df.iloc[0]['Deaths']:.2f}%")
output.append(f"Team Kills: {sub_df.iloc[0]['Team kill']}")
output.append(f"Jump Kills: {sub_df.iloc[0]['Jump kill']}")
output.append(longthing)
output.append(f"No. bomb plants: {sub_df.iloc[0]['Bomb planted']}")
output.append(f"No. bombs exploded: {sub_df.iloc[0]['Bomb exploded']}")
output.append(f"% of bombs exploded: {round(100*sub_df.iloc[0]['Bomb exploded']/sub_df.iloc[0]['Bomb planted'],2)}%")
output.append(f"No. bomb defusals: {sub_df.iloc[0]['Bomb defused']}")
output.append(longthing)
output.append(f"T Side Entry: {sub_df.iloc[0]['Entry kill']}")
output.append(f"T Side Entry win %: {sub_df.iloc[0]['Entry kill win %']}% ({round(df['Entry kill win %'].mean(),2)})")
output.append(f"CT Side Entry: {sub_df.iloc[0]['Entry hold kill']}")
output.append(f"CT Side Entry win %: {sub_df.iloc[0]['Entry hold kill win %']}% ({round(df['Entry hold kill win %'].mean(),2)})")

with open(f"{sub_df.iloc[0]['Name']}.txt", "w") as f:
    for string in output:
        print(string)
        f.write(string + "\n")
