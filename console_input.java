import java.io.*;
class console_input
{
public static void main(String args[])
{
int a=0;
BufferedReader br= new BufferedReader( new InputStreamReader(System.in));
try{
a=Integer.parseInt(br.readLine());
a=a+Integer.parseInt(br.readLine());
System.out.println(a);
}
catch(Exception ex)
{
System.out.println("Invalid Input");
}
}
}