# Write a Pandas program to join the two dataframes with matching records 
# from both sides where available.
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
    
    print(df1, "\n")
    print(df2, "\n")
    
    df3 = pd.merge(df1, df2, on="student_id", how="outer")
    print(df3, "\n")
    

if __name__ == "__main__":
    main()