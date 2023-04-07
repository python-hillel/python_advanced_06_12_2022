
def format_list_students(students):
    # string = '<br>'.join(str(student) for student in students)
    string = '<table>' \
             '<thead>' \
             '<tr>' \
             '<th>First name</th>' \
             '<th>Last name</th>' \
             '<th>Email</th>' \
             '<th>Birthday</th>' \
             '<th>City</th>' \
             '<th>Update</th>' \
             '</tr>' \
             '<thead>' \
             '<tbody>'
    for st in students:
        string += f'<tr>' \
                  f'<td>{st.first_name_1}</td>' \
                  f'<td>{st.last_name}</td>' \
                  f'<td>{st.email}</td>' \
                  f'<td>{st.birthday}</td>' \
                  f'<td>{st.city if st.city else ""}</td>' \
                  f'<td><a href="/students/update/{st.pk}/">Edit</a></td>' \
                  f'</tr>'

    string += '</tbody></table>'
    return string
