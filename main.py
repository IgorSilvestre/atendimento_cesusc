#!/usr/bin/env python3
import os

# CLASSES
class Student:
    def __init__ (self, full_name, birth_date, major, attendance, class_history):
        self.full_name = full_name
        self.birth_date = birth_date
        self.major = major
        self.attendance = attendance
        self.class_history = class_history

# FUNCTIONS
def create_folders ():
    if (os.path.isdir('resource_files') == False):
        os.mkdir ('resource_files')
    if (os.path.isdir ('resource_files/students') == False):
        os.mkdir ('resource_files/students')
    if (os.path.isdir ('resource_files/enrollment_certificates') == False):
        os.mkdir ('resource_files/enrollment_certificates')
    if (os.path.isdir ('resource_files/attendance_certificates') == False):
        os.mkdir ('resource_files/attendance_certificates')

def create_student ():
    student_full_name = input ('Nome Completo: ')
    student_name = Student (full_name = '', birth_date = '', major = '', attendance = '', class_history = '')
    student_name.full_name = student_full_name
    student_name.birth_date = input ('Data de nascimento (AAAA-MM-DD): ')
    student_name.major = input ('Curso: ')
    student_attendance = input ('Frequência (%): ')
    student_class_history = input ('Histórico Escolar: ')

    with open (f'resource_files/students/{student_full_name}.txt', 'w') as student_file:
        student_file.write ('NAME=' + student_name.full_name + "\n")
        student_file.write ('BIRTHDATE=' + student_name.birth_date + "\n")
        student_file.write ('MAJOR=' + student_name.major + '\n')
        student_file.write ('ATTENDANCE=' + student_attendance + '\n')
        student_file.write ('CLASSHISTORY=' + student_class_history)

    with open ('resource_files/students_list.txt', 'a') as students_list:
        students_list.write (student_full_name + '\n')

    print ('\n\nCadastro de estudante criado!')

def check_if_student_exists (student_name):
    with open ('resource_files/students_list.txt') as students_list:
        for lines in students_list:
            if (student_name == lines.rstrip('\n')):
                return True
    return False

def enrollment_certificate (student_name):
    if (check_if_student_exists (student_name) == False):
        print ('\n\nEstudante sem cadastro!')
        return 1
    
    # GET EMPLOYEE
    employee = input ('\nNome do funcionário responsável pelo atentimento: ')

    file_name = student_name
    with open (f'resource_files/students/{student_name}.txt', 'r') as student_file:
        data = {}
        for line in student_file:
            key, value = line.strip().split('=')
            data[key] = value
    student_name = data ['NAME']
    student_major = data ['MAJOR']

    default_text = f'A faculdade CESUSC declara por meio desde que o(a) estudante {student_name} esta atualmente matriculado(a) no curso de {student_major} em nossa instituição de ensino. Eu {employee}, me responsabilizo pela autenticidade desse documento.'
    with open (f'resource_files/enrollment_certificates/{file_name}-enrollment_certificate.txt', 'w') as enrollment_file:
        enrollment_file.write (default_text)
    
    print ('\n---------------')
    print (default_text)
    print ('---------------')
    print ('\n\nAtestado de matrícula criado!')
    
    return 0

def print_student_file (student_name):
    if (check_if_student_exists (student_name) == False):
        print ('\n\nEstudante sem cadastro!')
        return 1
    
    with open (f'resource_files/students/{student_name}.txt', 'r') as student_file:
        data = {}
        for line in student_file:
            key, value = line.strip().split('=')
            data[key] = value

    print ('\n---------------')
    print ('Nome Completo: ' + data ['NAME'])        
    print ('Data de Nascimento: ' + data ['BIRTHDATE'])        
    print ('Curso: ' + data ['MAJOR'])
    print ('Frenquência: ' + data ['ATTENDANCE'] + '%')
    print ('Histórico Escolar: ' + data ['CLASSHISTORY'])
    print ('---------------')

    return 0

def replace_file (old_file, new_file):
    os.remove (old_file)
    os.rename (new_file, old_file)

def update_student (student_name):
    if (check_if_student_exists (student_name) == False):
        print ('\n\nNenhum registro encontrado!')
        return 1
    print_student_file (student_name)

    new_name = input ('\nNovo nome: ')
    student_birth_date = input ('Nova data de nascimento (AAAA-MM-DD): ')
    student_major = input ('Novo curso: ')
    student_attendance = input ('Nova frequência (%): ')
    student_class_history = input ('Novo histórico escolar: ')
    
    with open (f'resource_files/students/{student_name}.txt', 'w') as student_file:
        student_file.write ('NAME=' + new_name + '\n')
        student_file.write ('BIRTHDATE=' + student_birth_date + '\n')
        student_file.write ('MAJOR=' + student_major + '\n')
        student_file.write ('ATTENDANCE=' + student_attendance + '\n')
        student_file.write ('CLASSHISTORY=' + student_class_history)

    if (student_name != new_name):
        # CHANGE STUDENT FILE NAME
        os.rename (f'resource_files/students/{student_name}.txt', f'resource_files/students/{new_name}.txt')

        # UPDATE STUDENTS BASE FILE
        with open ('resource_files/students_list.txt') as base_file:
            with open ('resource_files/temp.txt', 'w') as temp_file:
                for lines in base_file:
                    if (lines.rstrip ('\n') != student_name):
                        temp_file.write (lines)
                temp_file.write (new_name + '\n')
        replace_file ('resource_files/students_list.txt', 'resource_files/temp.txt') 
    return 0

def delete_student (student_name):
    if (check_if_student_exists (student_name) == False):
        print ('\n\nNenhum registro encontrado!')
        return 1
    print_student_file (student_name)

    # DOUBLE CHECK DELETION
    op = ''
    while (op != 's' and op != 'n'):
        op = input ('\nTem certeza que deseja deletar esse registro (s/n) ? ')
        op = op.lower ()

    if (op == 's'):
        os.remove (f'resource_files/students/{student_name}.txt')
        
        # UPDATE STUDENTS BASE FILE
        with open ('resource_files/students_list.txt') as base_file:
            with open ('resource_files/temp.txt', 'w') as temp_file:
                for lines in base_file:
                    if (lines.rstrip ('\n') != student_name):
                        temp_file.write (lines)
        replace_file ('resource_files/students_list.txt', 'resource_files/temp.txt') 

    return 0

def attendance_certificate (student_name):
    if (check_if_student_exists (student_name) == False):
        print ('\n\nEstudante sem cadastro!')
        return 1
    
    # GET EMPLOYEE
    employee = input ('\nNome do funcionário responsável pelo atendimento: ')

    with open (f'resource_files/students/{student_name}.txt') as student_file:
        data = {}
        for line in student_file:
            key, value = line.strip().split ('=')
            data [key] = value
    student_major = data ['MAJOR']
    student_attendance = data ['ATTENDANCE']

    default_text = f'A faculdade CESUSC declara por meio deste que o(a) estudante {student_name} esta atualmente matriculado(a) no curso de {student_major} com a porcentagem de frequência: {student_attendance}%. Eu {employee}, atendente da faculdade CESUSC, me responsabilizo pela autenticidade desse documento.'
    with open (f'resource_files/attendance_certificates/{student_name}-attendance_certificate.txt', 'w') as attendance_file:
        attendance_file.write (default_text)

    print ('\n---------------')
    print (default_text)
    print ('---------------')
    print ('\nAtestado de frequência criado!')

    return 0

def main():
    create_folders ()
    op = ''
    while (op != '1' and op != '2' and op != '3' and op != '4' and op != '5' and op != '6'):
        print ('PROGRAMA DE ATENDIMENTO CESUSC\n')
        print ('1. Nova matrícula')
        print ('2. Ajuste de registro do estudante')
        print ('3. Gerar atestado de matricula')
        print ('4. Gerar atestado frequência')
        print ('5. Deletar registro do estudante')
        print ('6. Procurar cadastro')
        print ('-----------------------------')
        print ('OBS: cadastro de matricula inclui: nome, data de nascimento, curso (preencher frequência e histórico escolar caso seja transferência). Pode adicionar frequência e histórico escolar do CESUSC em ajuste de matrícula.\n')
        op = input ('\nOpção: ')

    if (op == '1'):
        create_student ()
    
    if (op == '2'):
        student_name = True
        while (check_if_student_exists (student_name) == False):
            student_name = input ('\nNome do estudante a ser alterado o registro: ')
            if (check_if_student_exists (student_name) == False):
                print ('Nenhum registro encontrado! Veja se digitou algo incorretamente.')
        update_student (student_name)

    if (op =='3'):
        student_name = True
        while (check_if_student_exists (student_name) == False):
            student_name = input ('\nNome do estudante para gerar atestado de matrícula: ')
            if (check_if_student_exists (student_name) == False):
                print ('Nenhum registro encontrado! Veja se digitou algo incorretamente.')
        enrollment_certificate (student_name)
    
    if (op == '4'):
        student_name = True
        while (check_if_student_exists (student_name) == False):
            student_name = input ('\nNome do estudante para gerar atestado de frequência: ')
            if (check_if_student_exists (student_name) == False):
                print ('Nenhum registro encontrado! Veja se digitou algo incorretamente.')
        attendance_certificate (student_name)

    if (op == '5'):
        student_name = True
        while (check_if_student_exists (student_name) == False):
            student_name = input ('\nNome do estudante para deletar registro: ')
            if (check_if_student_exists (student_name) == False):
                print ('Nenhum registro encontrado! Veja se digitou algo incorretamente.')
        delete_student (student_name)

    if (op == '6'):
        student_name = True
        while (check_if_student_exists (student_name) == False):
            student_name = input ('\nNome do estudante que deseja procurar: ')
            if (check_if_student_exists (student_name) == False):
                print ('Nenhum registro encontrado! Veja se digitou algo incorretamente.')
        print_student_file (student_name)

if __name__ == '__main__': main()