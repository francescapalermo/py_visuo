import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
import utils
import custom_colors


def create_activity_plot(df, patient_list, month_list, location_list, column_patient='patient_id', column_date='date',
                         palette=custom_colors.ukdri_movement, max_yticks=15, savefig=True, save_path='./'):
    for patient in patient_list:
        for month in month_list:
            fig, ax = plt.subplots(figsize=(15, 5))
            for location in location_list:
                current_df = df[df[column_patient] ==
                                patient].reset_index(drop=True)
                current_df = current_df[current_df[column_date].dt.month.isin(
                    month)].reset_index(drop=True)
                current_df['date_more'] = current_df[column_date].astype(
                    str).str.split().str[0]
                current_df['time_of_day'] = pd.to_datetime(
                    '2000-01-01 ' + current_df['date'].dt.time.astype(str))
                tmp_input = current_df.query('location_name == @location')
                tmp_input = tmp_input.sort_values(
                    by=['date_more'], ascending=False)
                ax.scatter(tmp_input['time_of_day'],
                           tmp_input['date_more'], **palette[location])

            ax.set_xlim([pd.to_datetime('2000-01-01 00:00:00'),
                        pd.to_datetime('2000-01-01 23:59:59')])
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
            plt.xlabel("Time of the Day")
            yloc = plt.MaxNLocator(max_yticks)
            ax.yaxis.set_major_locator(yloc)
            plt.ylabel("Date")
            plt.suptitle(patient + '-' + str(month))
            plt.xlabel("Time of the Day")
            plt.ylabel("Day")
            utils.set_plot_features(fig, ax, show_legend=False)
            ax.legend(location_list, bbox_to_anchor=(
                1.05, 1), loc=2, borderaxespad=0.)
            if savefig:
                plt.savefig(save_path + '{}_activity.svg'.format(patient))


activity_df = pd.read_csv('./py_visual/data/Activity.csv')
activity_df['date'] = pd.to_datetime(activity_df['date'])
print(activity_df['location_name'].unique())
activity_df = activity_df.sort_values(by=['patient_id', 'date']).reset_index(drop=True)
location_list = ['Kitchen', 'Lounge', 'Bedroom', 'Bathroom', 'Front door']#'Fridge', 'Kettle', 'Toaster', 'Microwave','Front door']
month_list = [[4, 5, 6]]
patient_list = ['73f7c']

create_activity_plot(activity_df, patient_list, month_list, location_list, column_patient='patient_id', column_date='date',
                         palette=custom_colors.ukdri_movement, max_yticks=15, savefig=False)

plt.show()
print('Test')
