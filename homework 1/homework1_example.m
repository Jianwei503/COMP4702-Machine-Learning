function output = homework1_example(arr,n)
output = [];
idx = n;
while length(output)~= length(arr)
    while idx > length(arr)
        idx = idx - length(arr);
    end
    disp(idx);
    output = cat(2,output,arr(idx));
    n = n + 1;
    idx = idx + n;
end