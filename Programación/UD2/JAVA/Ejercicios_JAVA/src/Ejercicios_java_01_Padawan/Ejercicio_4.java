/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt 
 * to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java 
 * to edit this template
 */
package Ejercicios_java_01_Padawan;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * 
 * *************************ENUNCIADO*********************************
 * Ejercicio_4:Escribe un programa que lea dos números, calcule y 
 * muestre el valor de sus suma, resta, producto y división.
 * ********************************************************************
 * 
 */
//Importamos el java.util.Scanner
import java.util.Scanner;

public class Ejercicio_4 {
    public static void main(String[] args){
        
        double número_1, número_2, suma, resta, producto, división;
        //Declaro el objeto lector y entrada scanner
        Scanner lector = new Scanner(System.in);
        Scanner entrada = new Scanner(System.in);
        
        //Muestro en la pantalla el mensaje para introducir los números.
        System.out.println("Introduzca los números deseados");
        
        //utilizo lo siguiente para leer ambos números
        número_1 = lector.nextDouble();
        número_2 = entrada.nextDouble();
        
        //Realizo las operaciones convenientes del ejercicio
        suma = (número_1+número_2);
        resta = (número_1-número_2);
        división = (número_1/número_2);
        producto = (número_1*número_2);
        
        //Muestro en pantalla los resultados obtenidos
        System.out.println("El resultado de la suma es, "+suma+", el de "
                           + "la resta, "+ resta+", el de la división, "
                           +división+" y el de la multiplicación"+producto);
     }
}
