
/**
 * Write a description of class Execution here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Execution
{
   public static void main(String[] args){
       AppliedRepository ap = new AppliedRepository();
       
       // getting all the person
       System.out.println("Getting Persons");
       var ls = ap.getPeople();
       for(Person people : ls){
           System.out.println("Prson name  : "+people.GivenName);
        }
        
       // adding a person
       System.out.println("Adding Persons");
       Person p = new Person(100,"Kamal","Uddin",3000);
       ap.AddPerson(p);
       for(Person people : ls){
           System.out.println("Prson name  : "+people.GivenName);
        }
       
        // getting a single Person
        System.out.println("Getting  a single Persons");
        Person newPerson = ap.GetPerson(100);
        System.out.println("Prson name  : "+newPerson.GivenName);
        
        // update a single Person
        System.out.println("Updating  a single Persons");
        Person tmpPerson = new Person(999,"ornik","rahman",999);
        Person updatedPerson = ap.UpdatePerson(1,tmpPerson);
        for(Person people : ls){
           System.out.println("Prson name  : "+people.GivenName);
        }
        
        System.out.println("Deleting a single Persons");
        ap.DeletePerson(2);
        for(Person people : ls){
           System.out.println("Prson name  : "+people.GivenName);
        }
    }
    
    
    
}
