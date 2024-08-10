import requests
from datetime import datetime, timezone, timedelta

def get_bitcoin_address_details(address):
    url = f'https://api.blockcypher.com/v1/btc/main/addrs/{address}?includeSubaccounts=true&includeUnconfirmed=true'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Status code {response.status_code}")
        return {'error': 'Unable to fetch data'}

def format_transactions(transactions):
    formatted_transactions = []
    for i, tx in enumerate(transactions, start=1):
        # Parsing waktu konfirmasi transaksi
        date_time_utc = datetime.strptime(tx['confirmed'], '%Y-%m-%dT%H:%M:%S%z')

        # Mengonversi ke waktu Indonesia Barat (UTC+7)
        date_time_wib = date_time_utc.astimezone(timezone(timedelta(hours=7)))

        # Format tanggal dan waktu
        date_str = date_time_wib.strftime(f'({i}) %Y,%m,%d -- %H:%M')

        tx_id = tx['tx_hash']
        amount_satoshi = tx['value']

        # Format jumlah Satoshi dengan pemisah ribuan
        formatted_amount = f"{amount_satoshi:,}".replace(",", ".")

        # Tentukan apakah transaksi ini mengirim atau menerima
        if 'spent' in tx and tx['spent']:
            amount_str = f"- {formatted_amount} SAT"
        else:
            amount_str = f"+ {formatted_amount} SAT"

        formatted_transactions.append(f"{date_str}\n{tx_id} ==> {amount_str}\n")

    return formatted_transactions

def main():
    address = input('Masukkan alamat Bitcoin yang ingin Anda periksa: ')
    details = get_bitcoin_address_details(address)

    if 'error' in details:
        print(details['error'])
        return

    # Mendapatkan waktu UTC saat ini
    utc_now = datetime.utcnow()
    # Mengonversi waktu UTC ke WIB
    wib_now = utc_now + timedelta(hours=7)
    # Format waktu WIB
    generated_at_str = wib_now.strftime('%Y-%m-%d %H:%M WIB')

    print(f"\n==================================================")
    print(f"\n                ADDRESS STATEMENT\n")
    print(f"GENERATED AT {generated_at_str}")
    print(f"BLOCKCHAIN BITCOIN")
    print(f"ADDRESS ID {address}")
    print("\nBalance")

    # Format balance dengan pemisah ribuan
    formatted_balance = f"{details['final_balance']:,}".replace(",", ".")
    print(f"Bitcoin {formatted_balance} SAT")  # Display balance in SAT
    print("\nMAIN EVENTS")

    transactions = details.get('txrefs', [])
    formatted_transactions = format_transactions(transactions)

    if formatted_transactions:
        for tx in formatted_transactions:
            print(tx)
    else:
        print("No transactions found.")

if __name__ == "__main__":
    main()