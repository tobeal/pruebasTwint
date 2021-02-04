import json
import requests
import datetime
import pandas as pd


class TwinApiModel:
    def store(self,
              username: str = None,
              data: str = None,
              date_format='YYYY-MM-DD'):
        """
        Stores data using the DeepIntelligence API.
        Args:
           username
           tweets
           date_format
        """

        # check arguments
        if data.empty:
            raise ValueError(f'The providen DataFrame is empty')

        if data is None or username is None:
            raise ValueError(
                f'Is mandatory to provide not None values on parameters data ({data}), username ({username})'
            )

        # column order
        if column_order is None:
            column_order = data.columns

        # convert content to CSV
        try:
            streaming_data = data.to_csv(sep=',',
                                         index=send_with_index,
                                         columns=column_order)

            #data.to_csv(f'/home/gandalfran/desktop/{source}.csv',
            #            sep=',',
            #            index=send_with_index,
            #            columns=column_order)
            #print(column_order)
        except:
            raise ValueError(
                'Unable to convert DataFrame to CSV. Please, check the index, columns and the capability of serialization for the DataFrame fields.'
            )

        # send request
        uri = f'https://app.deepint.net/api/v1/workspace/{workspace}/source/{source}/instances'

        header = {'x-auth-token': token}

        body = {
            'replace': 'yes' if replace == True else 'no',
            'pk': pk,
            'separator': ',',
            'quotes': '"',
            'csv_header': 'yes',
            'json_fields': '',
            'date_format': date_format
        }

        files = [('file', ('file', streaming_data))]

        response = requests.post(uri, headers=header, data=body, files=files)
        if response.status_code != 200:
            raise ValueError(
                f'Unable to send data to deepint.net. Please, check the token, source, workspace, primary key and data. Also check the deepint.net status.'
                +
                f'\n\t\t Response(status={response.status_code},code={response.json()["code"]},message={response.json()["message"]})'
            )