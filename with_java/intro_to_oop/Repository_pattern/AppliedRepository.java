import java.util.*;
/**
 * Write a description of class AppliedRepository here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class AppliedRepository implements IPersonRepository
{
    ArrayList<Person> people = new ArrayList<Person>();
    Person p1 = new Person(1,"Tanvir","Rahman",3);
    Person p2 = new Person(2,"Ornob","Rahman",4);
    Person p3 = new Person(3,"Rajib","Rahman",5);
    Person p4 = new Person(4,"Habib","Rahman",5);
    Person p5 = new Person(5,"Tuhin","Rahman",10);
    
    public ArrayList<Person>getPeople(){
        people.add(p1);
        people.add(p2);
        people.add(p3);
        people.add(p4);
        people.add(p5);
        
        return people;
    }
    
    public Person GetPerson(int id){
        // getting the index
        Person actualPerson = null;
        for(Person person : people){
            if(person.Id == id){
                actualPerson = person;
                break;
            }
        }
    
           return actualPerson;
        
    }
    
    public void AddPerson(Person newPerson){
        people.add(newPerson);
    
    }
    
    public void DeletePerson(int id){
        // first get the person 
        // then delete the person
        Person tmpPerson = GetPerson(id);
        people.remove(tmpPerson);
        
        
    }
    public Person UpdatePerson(int id,Person updatedPerson){
        Person tmpPerson = GetPerson(id);
        tmpPerson.Id = updatedPerson.Id;
        tmpPerson.GivenName = updatedPerson.GivenName;
        tmpPerson.familyName = updatedPerson.familyName;
        tmpPerson.Rating = updatedPerson.Rating;
        
        return tmpPerson;
        
    
    }

}
