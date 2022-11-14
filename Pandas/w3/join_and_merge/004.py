# Write a Pandas program to append a list of dictioneries or series to a 
# existing DataFrame and display the combined data.
import pandas as pd


def main():
    
    df1 = pd.DataFrame(
        {
            'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
            'name': [
                'Danniella Fenton', 
                'Ryder Storey', 
                'Bryce Jensen', 
                'Ed Bernal', 
                'Kwame Morin'
            ], 
            'marks': [200, 210, 190, 222, 199]
        }
    )
    
    ds1 = pd.Series(data=['S6', 'Scarlette Fisher', 205],
                    index=['student_id', 'name', 'marks'])
    
    lst_of_dicts = [
        {'student_id': 'S6', 'name': 'Scarlette Fisher', 'marks': 203},
        {'student_id': 'S7', 'name': 'Bryce Jensen', 'marks': 207}
    ]
    print(df1, "\n")
    print(ds1, "\n")
    print(lst_of_dicts, "\n")
    
    df2 = pd.concat([df1, ds1.to_frame().T], ignore_index=True)
    print(df2, "\n")
    
    df3 = pd.DataFrame(lst_of_dicts)
    print(df3, "\n")
    
    df4 = pd.concat([df1, ds1.to_frame().T, pd.DataFrame(lst_of_dicts)],
                    ignore_index=True)
    print(df4)
    

if __name__ == "__main__":
    main()
