-- Define path to the blog_urls.txt file
set filePath to "/Users/isol/Documents/samablog/data/blog_urls.txt"

-- Read the file contents
set fileContent to read filePath

-- Split the content by newline to get individual URLs
set blogUrls to paragraphs of fileContent

-- Iterate over each URL and save the page as a PDF
repeat with blogUrl in blogUrls
    tell application "Safari"
        activate
        open location blogUrl
        set pageLoaded to false
        repeat until pageLoaded
            set pageLoaded to (do JavaScript "document.readyState" in document 1) is "complete"
            delay 1
        end repeat
        tell application "System Events" to keystroke "r" using {command down, shift down} -- Enter Reader Mode
        delay 2 -- wait a bit
        print document 1 with properties {target printer:"Save as PDF"}
        delay 5 -- time to let print dialog show up
        tell application "System Events"
            keystroke "p" using command down -- Invoke print dialog
            delay 2 -- time to let save as pdf dialog show up
            click menu button "PDF" of sheet 1 of window 1 of application process "Safari"
            click menu item "Save as PDF…" of menu of menu button "PDF" of sheet 1 of window 1 of application process "Safari"
            delay 2 -- wait a bit
            -- Construct the filename based on the blog's URL, now saving to the "posts" folder
            set theFileName to "/Users/isol/Documents/samablog/posts/" & (do shell script "basename " & quoted form of blogUrl) & ".pdf"
            set value of text field 1 of sheet 1 of window 1 of application process "Safari" to theFileName
            click button "Save" of sheet 1 of window 1 of application process "Safari"
        end tell
        delay 5 -- Give some time for the save process
    end tell
end repeat