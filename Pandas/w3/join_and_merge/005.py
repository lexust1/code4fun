# Write a Pandas program to join the two given dataframes along rows and merge 
# with another dataframe along the common column id.
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
    
    df2 = pd.DataFrame(
        {
            'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
            'name': [
                'Scarlette Fisher', 
                'Carla Williamson', 
                'Dante Morse', 
                'Kaiser William', 
                'Madeeha Preston'
            ], 
            'marks': [201, 200, 198, 219, 201]
        }
    )
    
    df3 = pd.DataFrame(
        {
            'student_id': [
                'S1', 
                'S2', 
                'S3', 
                'S4', 
                'S5', 
                'S7', 
                'S8', 
                'S9', 
                'S10', 
                'S11', 
                'S12', 
                'S13'
            ],
        'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]
        }
    )
    print(df1, "\n")
    print(df2, "\n")
    print(df3, "\n")
    
    df4 = pd.concat([df1, df2], ignore_index=True)
    print(df4, "\n")
    
    df5 = pd.merge(df3, df4, on="student_id")
    print(df5, "\n")


if __name__ == "__main__":
    main()
