
 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('loanmodel.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, ApplicantIncome,LoanAmount, Credit_History):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1   	
 
    LoanAmount = LoanAmount / 1000
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    return prediction

  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Loan Prediction App</h1> 
    </div> 
    <br>
    <p style ="color:white;text-align:center;">By Ana & Febi</p>  
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 

    ## Full Name
    fn = st.text_input('Full Name')
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    ApplicantIncome = st.number_input("Applicants monthly income") 
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 

        if result == 0:
            st.error(
                "Hello: " + fn +" "
                'according to our aalculations, you will not get the loan from bank'
            )
        else:
            st.success(
                "Hello: " + fn +" "
                'congratulations!! you will get the loan from bank'
            )
        print(LoanAmount)

    html_temp = """ 

    """
     
if __name__=='__main__': 
    main()