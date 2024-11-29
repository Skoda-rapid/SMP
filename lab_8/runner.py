from Business_Layer.commands import LoadDataCommand, ExtremeValuesCommand
from Persistence_Layer.visualizations import VisualizationReceiver
from Persistence_Layer.commands_visualization import BasicVisualizationCommand, ExtendedVisualizationCommand
from Presentation_layer.client import Client

def main():
    load_command = LoadDataCommand("Database_Layer/weather.csv")
    data = load_command.execute()

    if data is not None:
        print("Дані завантажені успішно.")

        extreme_values_command = ExtremeValuesCommand(data)
        extreme_values = extreme_values_command.execute()
        print("Екстремальні значення:")
        print(extreme_values)

        visualization_receiver = VisualizationReceiver(data)

        basic_visualization_command = BasicVisualizationCommand(visualization_receiver)
        basic_visualization_command.execute()

        extended_visualization_command = ExtendedVisualizationCommand(visualization_receiver)
        extended_visualization_command.execute()

        # Save combined visualizations
        visualization_receiver.save_combined_html("combined_visualization.html")
        visualization_receiver.save_combined_png("combined_visualization.png")

        client = Client()
        client.run_command(load_command)
    else:
        print("Не вдалося завантажити дані. Перевірте файл 'weather.csv'.")

if __name__ == "__main__":
    main()
