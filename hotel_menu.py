from hotel_sistema import Hotel, obter_input_nao_vazio

def main():
    hotel = Hotel()

    while True:
        print(f"""
=========================================================
{hotel.razao_social}
CNPJ: {hotel.cnpj}    
Endereço: {hotel.endereco}
Telefone: {hotel.telefone}
=========================================================

Escolha uma opção:

1. Ver suítes disponíveis
2. Ver todas as reservas
3. Fazer reserva
4. Encerrar reserva (Check-out)
5. Gerenciar clientes
6. Gerenciar reservas (Editar, Cancelar)
7. Gerenciar suítes
8. Sair
R: """, end="")
        menu_hotel = obter_input_nao_vazio("")

        match menu_hotel:
            case "1":
                hotel.listar_suites(apenas_disponiveis=True)
            
            case "2":
                hotel.consultar_reservas()
            
            case "3":
                hotel.fazer_reserva()
            
            case "4": 
                hotel.excluir_ou_cancelar_reserva(encerrar=True)
                
            case "5": 
                while True:
                    print("""
==================================
Menu de Gerenciamento de Clientes
==================================

Escolha uma opção:

1. Cadastrar cliente
2. Consultar clientes
3. Editar cliente
4. Excluir cliente
5. Voltar ao menu principal
R: """, end="")
                    menu_cliente = obter_input_nao_vazio("")  
                    match menu_cliente:
                        case "1":
                            hotel.cadastrar_cliente()
                        case "2":
                            hotel.listar_clientes()
                        case "3":
                            hotel.editar_cliente()
                        case "4":
                            hotel.excluir_cliente()
                        case "5":
                            print("\n🔙 Voltando ao menu principal...\n")
                            break
                        case _:
                            print("\n⚠️ Opção inválida. Tente novamente.\n")
            
            case "6": 
                while True:
                    print("""
==================================
Menu de Gerenciamento de Reservas
==================================

Escolha uma opção:

1. Editar reserva
2. Cancelar reserva
3. Voltar ao menu principal
R: """, end="")
                    menu_reservas = obter_input_nao_vazio("")  
                    match menu_reservas:
                        case "1":
                            hotel.editar_reserva()
                        case "2": 
                            hotel.excluir_ou_cancelar_reserva(encerrar=False)
                        case "3":
                            print("\n🔙 Voltando ao menu principal...\n")
                            break
                        case _:
                            print("\n⚠️ Opção inválida. Tente novamente.\n")
            
            case "7": 
                while True:
                    print("""
==================================
Menu de Gerenciamento de Suítes
==================================

Escolha uma opção:

1. Cadastrar Suíte
2. Consultar Todas as Suítes
3. Editar Suíte
4. Excluir Suíte
5. Voltar ao menu principal
R: """, end="")
                    menu_suites = obter_input_nao_vazio("") 
                    match menu_suites:
                        case "1":
                            hotel.cadastrar_suite()
                        case "2":
                            hotel.listar_suites(apenas_disponiveis=False)
                        case "3":
                            hotel.editar_suite()
                        case "4":
                            hotel.excluir_suite()
                        case "5":
                            print("\n🔙 Voltando ao menu principal...\n")
                            break
                        case _:
                            print("\n⚠️ Opção inválida. Tente novamente.")
            
            case "8":
                print("\n👋👋👋 Saindo...\n")
                break
            
            case _:
                print("\n⚠️ Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()



