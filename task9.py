marks={"max": 76,"romeo": 45,"kriya":90,"neha":67,"meha":54,"siyal":30,"kavya":49,"alex":95,"millet":39,"kiya":22}
name=str(input("enter the student name: "))
if name in marks:
    print(f"marks obtained by {name} are:")
    result=marks[name]
    print(result)
else:
    print("student not found")