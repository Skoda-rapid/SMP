import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from PIL import Image

class VisualizationReceiver:
    def __init__(self, data):
        self.data = data

    def basic_visualization(self):
        self.data.plot(kind='bar')
        plt.show()

    def extended_visualization(self):
        if len(self.data.columns) >= 2:
            col1 = self.data.columns[0]
            col2 = self.data.columns[1]
            plt.scatter(self.data[col1], self.data[col2])
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title('Extended Visualization: Scatter Plot')
            plt.show()
        else:
            print("Not enough columns for extended visualization.")

    def save_combined_html(self, filename):
        if len(self.data.columns) > 1:
            # Basic visualization as HTML
            long_form_data = pd.melt(self.data, id_vars=self.data.columns[0], value_vars=self.data.columns[1:])
            fig1 = px.bar(long_form_data, x=self.data.columns[0], y='value', color='variable',
                          title='Basic Visualization: Bar Plot')
            html1 = fig1.to_html(full_html=False)

            # Extended visualization as HTML
            if len(self.data.columns) >= 2:
                fig2 = px.scatter(self.data, x=self.data.columns[0], y=self.data.columns[1],
                                  title='Extended Visualization: Scatter Plot')
                html2 = fig2.to_html(full_html=False)

                # Combine both HTMLs into one file
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write('<html><head><title>Combined Visualizations</title></head><body>')
                    f.write(html1)
                    f.write(html2)
                    f.write('</body></html>')
                print(f"Combined HTML visualization saved as {filename}")
            else:
                print("Not enough columns for extended visualization.")

    def save_combined_png(self, filename):
        basic_filename = "basic_visualization.png"
        extended_filename = "extended_visualization.png"
        
        # Save individual images
        self.save_basic_visualization_png(basic_filename)
        self.save_extended_visualization_png(extended_filename)

        # Open images and combine them side-by-side
        try:
            img1 = Image.open(basic_filename)
            img2 = Image.open(extended_filename)

            # Create a new image with width equal to the sum of both images' widths
            total_width = img1.width + img2.width
            max_height = max(img1.height, img2.height)
            combined_image = Image.new('RGB', (total_width, max_height))

            # Paste images side-by-side
            combined_image.paste(img1, (0, 0))
            combined_image.paste(img2, (img1.width, 0))

            # Save the combined image
            combined_image.save(filename)
            print(f"Combined PNG visualization saved as {filename}")
        except FileNotFoundError as e:
            print(f"Error combining images: {e}")

    def save_basic_visualization_png(self, filename):
        if len(self.data.columns) > 1:
            long_form_data = pd.melt(self.data, id_vars=self.data.columns[0], value_vars=self.data.columns[1:])
            long_form_data.pivot(index=self.data.columns[0], columns='variable', values='value').plot(kind='bar')
            plt.title('Basic Visualization: Bar Plot')
            plt.savefig(filename)
            plt.close()
            print(f"Basic visualization saved as PNG: {filename}")
        else:
            print("Not enough columns for basic visualization.")

    def save_extended_visualization_png(self, filename):
        if len(self.data.columns) >= 2:
            col1 = self.data.columns[0]
            col2 = self.data.columns[1]
            plt.scatter(self.data[col1], self.data[col2])
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title('Extended Visualization: Scatter Plot')
            plt.savefig(filename)
            plt.close()
            print(f"Extended visualization saved as PNG: {filename}")
        else:
            print("Not enough columns for extended visualization.")
