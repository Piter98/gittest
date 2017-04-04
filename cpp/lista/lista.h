typedef struct ELEMENT
{
    int value;
    ELEMENT *next;

}ELEMENT;

typedef struct HEADER
{
    ELEMENT *head;
    ELEMENT *tail;
}

class Lista
{
    private:
        HEADER header;
    public:
        Lista(); // konstruktor
        ~Lista(); // dekonstruktor
        void Dodaj(int value);
        bool Wstaw(int value, int position);
        int Usun();
        bool Usun(int);
        void Wyswietl();
        bool Pusta();
}
