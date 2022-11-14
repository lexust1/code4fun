# Write a Pandas program to append rows to an existing DataFrame and 
# display the combined data.

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
    
    ds1 = pd.Series(['S6', 'Scarlette Fisher', 205], 
                    index=['student_id', 'name', 'marks'])
    print(df1, "\n")
    print(ds1, "\n")
    
    df2 = df1.append(ds1, ignore_index=True)
    print(df2, "\n")
    
    df3= pd.concat([df1, ds1.to_frame().T], ignore_index=True)
    print(df3)
    

if __name__ == "__main__":
    main()