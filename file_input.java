import java.io.*;
class file_input
{
public static void main(String args[])throws IOException
{
String path="";
String line="";
int a=0;
BufferedReader br= new BufferedReader( new InputStreamReader(System.in));
path=br.readLine();
try (BufferedReader br1 = new BufferedReader(new FileReader(path)))
 {
while ((line = br1.readLine()) != null)
 {
   a=a+ Integer.parseInt(line);   
  }
System.out.println(a);
}
catch(Exception ex)
{
System.out.println("Invalid Input");
}

}
}