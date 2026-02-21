import os
import re
from bs4 import BeautifulSoup

def transform_html_file(file_path):
    print(f"Transforming: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # 1. Add app-container wrapper if it doesn't exist
    if not soup.find(class_='app-container'):
        body = soup.find('body')
        if body:
            # Create the new structure
            container = soup.new_tag('div', attrs={'class': 'app-container'})
            
            # Keep the sidebar (it's already a direct child of body usually)
            sidebar = soup.find('nav', class_='sidebar')
            if sidebar:
                sidebar.extract()
                container.append(sidebar)
            
            # Create main-wrapper
            wrapper = soup.new_tag('div', attrs={'class': 'main-wrapper'})
            
            # Move existing main into wrapper, or create it if missing
            main = soup.find('main', class_='main-content')
            if main:
                main.extract()
                wrapper.append(main)
            else:
                main = soup.new_tag('main', attrs={'class': 'main-content'})
                wrapper.append(main)
                
            # Create TOC sidebar
            toc = soup.new_tag('aside', attrs={'class': 'toc-sidebar'})
            toc_title = soup.new_tag('div', attrs={'class': 'toc-title'})
            toc_title.string = "On this page"
            toc.append(toc_title)
            toc_list = soup.new_tag('ul', attrs={'class': 'toc-list', 'id': 'toc-list'})
            toc.append(toc_list)
            
            wrapper.append(toc)
            container.append(wrapper)
            
            # Clear body and append container
            body.clear()
            body.append(container)

    # 2. Add Mobile Header
    if not soup.find(class_='mobile-header'):
        m_header = soup.new_tag('div', attrs={'class': 'mobile-header'})
        m_btn = soup.new_tag('button', attrs={'class': 'menu-toggle', 'onclick': 'toggleSidebar()'})
        m_btn.string = "☰"
        m_logo = soup.new_tag('span', attrs={'class': 'logo'})
        m_logo.string = "☁️ AIP-C01"
        m_header.append(m_btn)
        m_header.append(m_logo)
        soup.body.insert(0, m_header)

    # 3. Transform Slides to Sections & Build TOC
    slides_container = soup.find(class_='slides-container')
    toc_list = soup.find(id='toc-list')
    
    if slides_container and toc_list:
        toc_list.clear()
        slides = slides_container.find_all(class_='slide')
        
        for slide in slides:
            slide_id = slide.get('id', '')
            slide_num_div = slide.find(class_='slide-number')
            slide_num_text = slide_num_div.text if slide_num_div else "Slide"
            
            content_div = slide.find(class_='slide-content')
            if not content_div:
                continue
                
            # Identify title (usually the first <p>)
            first_p = content_div.find('p')
            title_text = "Section"
            if first_p:
                title_text = first_p.text.strip()
                # If the title is just a slide number or generic, try harder
                if not title_text or len(title_text) < 3:
                     title_text = f"Topic {slide_id}"
                
                # Check for footer noise and remove it
                for p in content_div.find_all('p'):
                    t = p.text.strip().lower()
                    if 'sundog-education.com' in t or 'datacumulus.com' in t or 'all rights reserved' in t:
                        p.decompose()

                # Add to TOC
                anchor = slide_id
                toc_item = soup.new_tag('li')
                toc_link = soup.new_tag('a', href=f"#{anchor}")
                toc_link.string = title_text[:40] + ('...' if len(title_text) > 40 else '')
                toc_item.append(toc_link)
                toc_list.append(toc_item)
                
                # Update slide to section
                slide['class'] = 'doc-section'
                new_h2 = soup.new_tag('h2', id=anchor)
                new_h2.string = title_text
                
                # If we promote first_p to h2, remove it from content
                first_p.decompose()
                slide.insert(0, new_h2)
            
        # Optional: Change slides-container to doc-container
        slides_container['class'] = 'doc-container'

    # 4. Clean up existing headers
    top_bar = soup.find(class_='top-bar')
    if top_bar:
        top_bar.decompose()
        
    section_hero = soup.find(class_='section-hero')
    if section_hero:
        # Keep the h1, but clean up the rest
        h1 = section_hero.find('h1')
        subtitle = section_hero.find(class_='section-subtitle')
        stats = section_hero.find(class_='section-stats')
        if stats: stats.decompose()
        
    # 5. Add JS for sidebar
    scripts = soup.find_all('script')
    has_script = False
    for s in scripts:
        if 'toggleSidebar' in s.text:
            has_script = True
            break
            
    if not has_script:
        new_script = soup.new_tag('script')
        new_script.string = """
        function toggleSidebar() {
            document.querySelector('.sidebar').classList.toggle('open');
        }
        """
        soup.body.append(new_script)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

def main():
    base_dir = '/Users/dhee/git/aws-genai-aip-c01'
    for filename in os.listdir(base_dir):
        if filename.endswith('.html') and filename != 'index.html':
            transform_html_file(os.path.join(base_dir, filename))

if __name__ == "__main__":
    main()
