import csv
from pathlib import Path
import os
from datetime import datetime

class OutputHandler:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.output_dir = self.base_dir / "data" / "output"

    def save_results(self, results, language):
        os.makedirs(self.output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{language}_results_{timestamp}.csv"
        output_path = os.path.join(self.output_dir, filename)

        with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(results.columns) 

            for row in results.iter_rows():
                writer.writerow(row)

        return output_path