public class MyClass
{
    private string _companyName;

    public string CompanyName
    {
        get => _companyName;
        set => _companyName = value;
    }
    
    private int _customerId;

    public int CustomerId
    {
        get => _customerId;
        set => _customerId = value;
    }
    
    private string _emailAddress;

    public string EmailAddress
    {
        get => _emailAddress;
        set => _emailAddress = value;
    }
    
    private string _firstName;

    [MaxLength(50)]
    public string FirstName
    {
        get => _firstName;
        set => _firstName = value;
    }
    
    private string _lastName;

    public string LastName
    {
        get => _lastName;
        set => _lastName = value;
    }
    
    private string _phoneNumber;

    public string PhoneNumber
    {
        get => _phoneNumber;
        set => _phoneNumber = value;
    }
    
}