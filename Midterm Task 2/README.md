let
    Source = Excel.Workbook(File.Contents("C:\Users\Computer LAB\Downloads\Uncleaned_DS_jobs.xlsx"), null, true),
    #"Uncleaned_DS_jobs (2)_Sheet" = Source{[Item="Uncleaned_DS_jobs (2)",Kind="Sheet"]}[Data],
    #"Promoted Headers" = Table.PromoteHeaders(#"Uncleaned_DS_jobs (2)_Sheet", [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"index", Int64.Type}, {"Job Title", type text}, {"Salary Estimate", type text}, {"Job Description", type text}, {"Rating", type number}, {"Company Name", type text}, {"Location", type text}, {"Headquarters", type any}, {"Size", type any}, {"Founded", Int64.Type}, {"Type of ownership", type any}, {"Industry", type any}, {"Sector", type any}, {"Revenue", type any}, {"Competitors", type any}}),
    #"Extracted Text Before Delimiter" = Table.TransformColumns(#"Changed Type", {{"Salary Estimate", each Text.BeforeDelimiter(_, "("), type text}}),
    #"Sorted Rows" = Table.Sort(#"Extracted Text Before Delimiter",{{"Salary Estimate", Order.Ascending}}),
    #"Inserted Text Between Delimiters" = Table.AddColumn(#"Sorted Rows", "Min Sal", each Text.BetweenDelimiters([Salary Estimate], "$", "K"), type text),
    #"Inserted Text Between Delimiters1" = Table.AddColumn(#"Inserted Text Between Delimiters", "MAX Sal", each Text.BetweenDelimiters([Salary Estimate], "$", "K", 1, 0), type text),
    #"Added Custom" = Table.AddColumn(#"Inserted Text Between Delimiters1", "Role Type", each if Text.Contains([Job Title], "Data Scientist") then
"Data Scientist"
else if Text.Contains([Job Title], "Data Analyst") then
"Data Analyst"
else if Text.Contains([Job Title], "Data Engineer") then
"Data Engineer"
else if Text.Contains([Job Title], "Machine Learning") then
"Machine Learning Engineer"
else
"other"),
    #"Changed Type1" = Table.TransformColumnTypes(#"Added Custom",{{"Role Type", type text}}),
    #"Added Custom1" = Table.AddColumn(#"Changed Type1", "Custom", each if [Location]= "New Jersey" then ", NJ"
else if [Location] = "Remote" then ", other"
else if [Location]= "United States" then ", other"
else if [Location]= "Texas" then ", TX"
else if [Location]= "Patuxent" then ", MA"
else if [Location]= "California" then ", CA"
else if [Location]= "Utah" then ", UT"
else [Location]),
    #"Split Column by Delimiter" = Table.SplitColumn(#"Added Custom1", "Custom", Splitter.SplitTextByDelimiter(",", QuoteStyle.Csv), {"Custom.1", "Custom.2"}),
    #"Changed Type2" = Table.TransformColumnTypes(#"Split Column by Delimiter",{{"Custom.1", type text}, {"Custom.2", type text}}),
    #"Reordered Columns" = Table.ReorderColumns(#"Changed Type2",{"index", "Job Title", "Salary Estimate", "Job Description", "Rating", "Company Name", "Location", "Custom.1", "Custom.2", "Headquarters", "Size", "Founded", "Type of ownership", "Industry", "Sector", "Revenue", "Competitors", "Min Sal", "MAX Sal", "Role Type"}),
    #"Removed Columns" = Table.RemoveColumns(#"Reordered Columns",{"Location"}),
    #"Renamed Columns" = Table.RenameColumns(#"Removed Columns",{{"Custom.1", "Location"}, {"Custom.2", "Abbreviation"}}),
    #"Replaced Value" = Table.ReplaceValue(#"Renamed Columns","Anne Arundel","MA",Replacer.ReplaceText,{"Abbreviation"}),
    #"Renamed Columns1" = Table.RenameColumns(#"Replaced Value",{{"Abbreviation", "State Abbreviations"}}),
    #"Split Column by Delimiter1" = Table.SplitColumn(Table.TransformColumnTypes(#"Renamed Columns1", {{"Size", type text}}, "en-PH"), "Size", Splitter.SplitTextByDelimiter("employees", QuoteStyle.Csv), {"Size.1", "Size.2"}),
    #"Changed Type3" = Table.TransformColumnTypes(#"Split Column by Delimiter1",{{"Size.1", type text}, {"Size.2", type text}}),
    #"Removed Columns1" = Table.RemoveColumns(#"Changed Type3",{"Size.2"}),
    #"Sorted Rows1" = Table.Sort(#"Removed Columns1",{{"Size.1", Order.Ascending}}),
    #"Duplicated Column" = Table.AddColumn(#"Sorted Rows1", "MinCompanySize", each [Size.1], type text)
in
    #"Duplicated Column"
