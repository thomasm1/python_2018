# library & dataset  color palette with Seaborn
import seaborn as sns
df = sns.load_dataset('iris')
# --- Use the 'palette' argument of seaborn
sns.lmplot( x="sepal_length", y="sepal_width", data=df, fit_reg=False, hue='species',
legend=False, palette="Set1")
plt.legend(loc='lower right')
# --- Use a handmade palette
flatui = ["#9b59b6", "#3498db", "orange"]
sns.set_palette(flatui)
sns.lmplot( x="sepal_length", y="sepal_width", data=df, fit_reg=False, hue='species',
legend=False)

